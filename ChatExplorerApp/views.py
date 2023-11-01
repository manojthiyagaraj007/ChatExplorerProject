from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from ChatExplorerApp.Models.chatmodel import ChatModel
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Max

from ChatExplorerApp.Models.usermodel import UserModel

# Create your views here.


def index(request):
    
    return render(request,"index.html")


def save_to_db(request):
    # # Change 'your_file_path.csv' to the actual path of your CSV file
    # file_path = './Files/ChatExport.json'
    try:
    #     with open(file_path, 'r') as file:
    #         json_data = json.load(file)

    #     # Loop through JSON data and save to the database
    #     for item in json_data:
    #         chat_instance = ChatModel(
    #             sessionId=item['sessionId'],
    #             userId=item['userId'],
    #             messageId=item['messageId'],
    #             message=item['message'],
    #             createdAt=item['createdAt'],
    #             updatedAt=item['updatedAt'],
    #         )
    #         chat_instance.save()


        user_json_file = './Files/Users.json'
        with open(user_json_file, 'r') as file:
            data = json.load(file)  # Use json.load to load the JSON data

            for item in data:
                user = UserModel(
                    userId=item['userId'],
                    orgId=item['orgId'],
                    email=item['email'],
                    firstName=item['firstName'],
                    lastName=item['lastName'],
                    createdAt=item['createdAt'],
                    updatedAt=item['updatedAt'],
                    metadata=item['metadata']
                )
                user.save()
    except FileNotFoundError:
        print(f'File not found')
    except json.JSONDecodeError:
        print(f'Invalid JSON format in the file')
        

    return HttpResponse("Data saved to the database.")


def signup(request):
    user_exixt_check = False 
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        print(username,email,password)
        if User.objects.filter(username=username).exists():
            # Handle the case where the user already exists
            print("User already exists.")
            user_exixt_check = True  # Set the flag to True
            return render(request,"index.html",{'user_exist': user_exixt_check})
        else:
            # Create a new user
            user = User.objects.create_user(username, email, password)
            
            # Optionally, you can log in the user after signup
            # authenticate the user
            user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("User created and logged in.")
    return render(request,"index.html")


def login_view(request):
    invalid_login = False 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username,password)
        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login the user
            login(request, user)
            print("User logged in.")
            # Redirect to a success page or any other logic you want
            return redirect('ChatExplorerApp:chat')

        else:
            # Handle invalid login credentials
            print("Invalid login credentials.")
            invalid_login = True  # Set the flag to True
            return render(request,"index.html",{'invalid_login': invalid_login})

    return render(request,"signup.html")


# Api Method for Getting All Session Data
@api_view(['GET'])
def getsessions(request,user_id):
    session_list = ChatModel.objects.filter(userId=user_id).values('sessionId').annotate(latest_created=Max('createdAt'))
    sessions_data = [{'sessionId': session['sessionId'], 'latest_created': session['latest_created']} for session in session_list]
    return JsonResponse(sessions_data, safe=False)


# Method for render index view
def chat(request):
    user_list = UserModel.objects.all()
    print(user_list)
    return render(request,'chat.html',{'user_list':user_list})

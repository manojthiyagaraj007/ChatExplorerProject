from django.db import models


#Created Model 
class ChatModel(models.Model):
        sessionId = models.CharField(max_length=100)
        userId = models.CharField(max_length=100)
        messageId = models.CharField(max_length=100)
        message = models.CharField(max_length=100)
        createdAt = models.DateTimeField()
        updatedAt = models.DateTimeField()

        def __str__(self):
                return self.messageId  # Return the email as the model's string representation



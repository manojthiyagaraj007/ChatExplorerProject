window.onload = function () {

    let current_domain = "http://127.0.0.1:8000/"
    var selectedValue = $('#userSelect').val();
    console.log(selectedValue)
    console.log("selectedvalue")

    handleSelectChange();

    // Api call Method

    function api_call(url){
        return new Promise(function (resolve, reject) {
            fetch(url)
              .then(response => response.json())
              .then(data => {
                resolve(data);
              })
              .catch(error => {
                reject(error);
              });
          });
    }


    
    // Add a change event listener to the select box
    $('#userSelect').on('change', handleSelectChange);

    // Function to handle the change event
    function handleSelectChange() {
        // Get the selected value
        var selectedValue = $('#userSelect').val();
        console.log(selectedValue)
        let url = `${current_domain}/getsessions/${selectedValue}`;
        const sessionContainer = $('#session-container');
        sessionContainer.empty();
        $('#session-alert').addClass('d-none');
        $('.loader').removeClass('d-none');
        api_call(url)
            .then(session_list => {
                // The first function has completed, and you have the session_list
                RenderSessionDetails(session_list);
                
            })
            .catch(error => {
                // Handle any errors from the API call
                console.error("API call error:", error);
            });
    }


    // For render Session Data

    function RenderSessionDetails(data){
        const sessionContainer = $('#session-container');
        $('.loader').addClass('d-none');
        sessionContainer.empty();
        if(data.length == 0){
            $('#session-alert').removeClass('d-none');
        }
        else{
            $('#session-alert').addClass('d-none');
        }
        $.each(data, function (key, value) {
            // Parse the original date string
            const originalDate = new Date(value.latest_created);

            // Format the date as "Dec 9, 8:35 PM"
            const formattedDate = originalDate.toLocaleString('en-US', {
            month: 'short',  // Short month name (e.g., Dec)
            day: 'numeric',   // Day of the month (e.g., 9)
            hour: 'numeric',  // Hour (e.g., 8)
            minute: '2-digit', // Minutes (e.g., 35)
            hour12: true      // Use 12-hour clock (AM/PM)
            });
            const sessionItem = `
            <div class="d-lg-flex align-items-center justify-content-between py-1 session-item-flex mb-1">
                <div>
                <h6 class="session-item-text">${value.sessionId}</h6>
                </div>
                <div>
                <h6 class="text-muted session-item-text">${formattedDate}</h6>
                </div>
            </div>
            `;
            sessionContainer.append(sessionItem);
        });
    }

};

function toggleCard(cardId) {
    // Hide all cards
    document.getElementById('signupcard').style.display = 'none';
    document.getElementById('logincard').style.display = 'none';

    // Show the selected card
    document.getElementById(cardId).style.display = 'block';
}

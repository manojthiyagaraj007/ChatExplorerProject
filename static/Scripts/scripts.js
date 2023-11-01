function toggleCard(cardId) {
    // Hide all cards
    document.getElementById('signupcard').style.display = 'none';
    document.getElementById('logincard').style.display = 'none';

    // Show the selected card
    document.getElementById(cardId).style.display = 'block';
}
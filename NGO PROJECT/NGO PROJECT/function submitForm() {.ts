function submitForm() {
    const uname = document.getElementById('uname').value;
    const email = document.getElementById('email').value;
    const number = document.getElementById('number').value;

    // Client-side validation
    if (!uname || !email || !number) {
        alert('Please fill in all fields.');
        return;
    }

    // Additional validation (e.g., email format)
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert('Please enter a valid email address.');
        return;
    }

    // Create JSON data
    const jsonData = {
        uname: uname,
        email: email,
        number: number
    };

    // Make a POST request to your Flask backend
    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(jsonData),
    })
    .then(response => response.json())
    .then(data => {
        // Display the response message
        document.getElementById('message').innerText = data.message;
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

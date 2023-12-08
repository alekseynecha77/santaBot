function sendQuery() {
    var userInput = document.getElementById('userQuery').value;

    fetch('/ask-santa', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('response').innerText = data.response; // Assuming the server responds with a JSON object that has a 'response' field
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}


import requests

# Updated URL to target the specific endpoint for Santa queries
url = 'http://127.0.0.1:5000/'

# Data to be sent in the request
data = {"query": "tell me 3 top hottest planets."}

try:
    # Sending a POST request to the server
    response = requests.post(url, json=data)
    response.raise_for_status()  # Raises an HTTPError for unsuccessful status codes

    # Print the response from the server
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Handle HTTP errors
except Exception as err:
    print(f'An error occurred: {err}')  # Handle other exceptions

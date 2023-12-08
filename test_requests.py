import requests

url = 'http://127.0.0.1:5000/'
data = {"query": "tell me 3 top hottest planets."}

try:
    response = requests.post(url, json=data)
    response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
    print(response.text)
except requests.exceptions.HTTPError as http_err:
    print(f'HTTP error occurred: {http_err}')  # Python 3.6+
except Exception as err:
    print(f'An error occurred: {err}')

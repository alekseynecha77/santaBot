import requests

url = 'http://127.0.0.1:5000/ask-santa'
data = {"query": "tell me 3 top hottest planets."}
response = requests.post(url, json=data)

print(response.text)
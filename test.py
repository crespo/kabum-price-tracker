import requests

BASE = "http://127.0.0.1:5000/"

response = requests.put(BASE + 'product/102274')
print(response.json())

input()
response = requests.get(BASE + 'product/102274')
print(response.json())

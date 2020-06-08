import requests

response = requests.get('https://api.github.com/users')

for r in response.json():
    print(r)

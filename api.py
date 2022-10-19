import requests
response = requests.get("https://x-colors.herokuapp.com/api/random")
print(response.json())
import requests

response = requests.get('http://headers.scrapeops.io/v1/user-agents?api_key=0b7ee11e-6427-4178-a3cc-d0b0cb2df7a5')

print(response.json())


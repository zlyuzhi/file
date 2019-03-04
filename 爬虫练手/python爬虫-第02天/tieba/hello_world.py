import requests
response = requests.get('http://www.baisu.com/')
print(response.content.decode('utf-8'))


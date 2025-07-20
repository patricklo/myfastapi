import requests

url = "http://localhost:8888/user/1002"
response = requests.get(url)
print(response.text)
print(response.status_code)
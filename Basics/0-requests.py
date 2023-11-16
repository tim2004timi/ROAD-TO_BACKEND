import requests


URL = "https://httpbin.org/get"

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(URL, params=payload)

print(response.url)
print(response.text)

import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.post(endpoint,json={"title":'ABC',"content":"Hello world","price":"abc123"})
print(get_response.json())
print(get_response.status_code)
# print(get_response.text)
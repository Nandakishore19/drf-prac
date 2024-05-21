import requests
headers = {
    "Authorization": "Bearer f38f8b17b6fbdb0e1f1add312ad1254c9441a75e"
}
endpoint = "http://localhost:8000/api/products/"
data = {
    "title":"Field Done wonderful",
}
get_response = requests.post(endpoint,json=data,headers=headers)
print(get_response.json())

import requests

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title":"Hello world",
    "price":1299
}
get_response = requests.put(endpoint,json=data)
print(get_response.json())

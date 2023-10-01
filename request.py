import requests

# Exemplo de solicitação GET
response_get = requests.get("http://localhost:5000/api/get_example")
print(response_get.json())

# Exemplo de solicitação POST com dados JSON
data = {"message": "Olá, servidor Flask!"}
response_post = requests.post(
    "http://localhost:5000/api/post_example", json=data)
print(response_post.json())

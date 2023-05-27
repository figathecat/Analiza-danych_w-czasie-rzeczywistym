import requests

response = requests.get("http://127.0.0.1:5000/abc?length_sepal=4.6&length_petal=3.2")
print(response.content)
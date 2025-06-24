import requests

data = {"age": 45, "salary": 85000}
response = requests.post("http://127.0.0.1:5000/predict", json=data)
print(response.json())

import requests

url =  "http://localhost:8000/predict"
filename = "test.jpg"

file = {'file': open(filename, 'rb')}
res = requests.post(url=url, files=file) 

print(res.json())

import requests

msg = "hey"
req = requests.post("http://127.0.0.1:5000/",data=msg)
print(req)
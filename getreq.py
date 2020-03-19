from flask import Flask
import requests
import json

r = requests.get("http://127.0.0.1",params=None)
print("GET:- ",r.status_code, r.content, r.headers)
la = {"language":"Ruby"}
la = json.dumps(la)

r = requests.post("http://127.0.0.1/lang", data = la)

print(r.text)
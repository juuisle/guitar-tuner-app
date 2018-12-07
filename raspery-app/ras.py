import requests

ROOT_URL = "http://127.0.0.1:5000/selected"

r = requests.get(ROOT_URL)

print r.text

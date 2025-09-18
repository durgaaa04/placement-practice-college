# https://restful-booker.herokuapp.com/apidoc/

import json
import requests


url = "https://simple-books-api.click/books"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
id = response.json()[2]['id']
print(id)

status = response.loads(response.text)['status']
print(status)
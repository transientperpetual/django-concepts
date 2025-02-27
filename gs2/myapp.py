import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    'id': 148,
    'name': 'Sourabh',
    'roll': 17,
    'city': 'Mumbai' 
}

json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data)
print(r.json())
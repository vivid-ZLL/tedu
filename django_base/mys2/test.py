import json

import requests

data = json.dumps({'name': 'roy','lord':'alice'})
print(data)
requests.post(
    url='http://0.0.0.0:8000/connectdb',
    data=data,
    # headers={'Content-Type': 'application/x-www-form-urlencoded'}
    headers={'Content-Type': 'application/x-www-form-urlencoded'}

)

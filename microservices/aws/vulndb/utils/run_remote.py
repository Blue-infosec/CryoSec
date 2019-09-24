#!/usr/bin/env python3.7
import requests
from payloads import payload
headers = {'Content-Type': 'application/json'}
url='https://omdul8jp29.execute-api.us-west-2.amazonaws.com/default/vulndb'
r = requests.post(
        url,
        headers=headers,
        data=payload)
#r = requests.get(
#        url,
#        headers=headers,
#        data=payload)

print(r.json())

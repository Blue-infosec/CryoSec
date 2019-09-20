#!/usr/bin/env python3.7

import requests
url='https://lmelndhslg.execute-api.us-west-2.amazonaws.com/Prod/genckl'
data='''

'''
x = requests.post(url,data,)

print(x.text)

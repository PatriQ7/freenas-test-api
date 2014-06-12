#!/usr/local/bin/python

import requests
import json

service = 'afp'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "afp_srv_guest": True,
          "afp_srv_connections_limit": 60
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/' + service + '/' 

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)

result = json.loads(r.text)
for items in result:
  print items,':',result[items]



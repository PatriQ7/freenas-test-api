#!/usr/local/bin/python

import requests
import json

headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "afp_srv_guest": True,
          "afp_srv_connections_limit" : 60
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/afp/' 

r = requests.put(url,auth=auth,headers=headers,data=json.dumps(payload))

print r.status_code
result = json.loads(r.text)
for items in result:
  print items,':',result[items]



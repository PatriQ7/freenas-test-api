#!/usr/local/bin/python

import requests
import json

service = 'globalconfiguration'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "iscsi_maxconnect": 15
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/iscsi/' + service 
r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)
print r.status_code
result = json.loads(r.text)
for items in result:
  print items+':',result[items]
r = requests.get(url, auth = auth)
result = json.loads(r.text)
#for items in result:
#  print items+':',result[items]

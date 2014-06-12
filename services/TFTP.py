#!/usr/local/bin/python

import requests
import json

service = 'tftp'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "tftp_port": 75,
          "tftp_directory": "/mnt/tank0"
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/' + service + '/' 

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)
#r = requests.get(url, auth = auth)
print r.status_code
result = json.loads(r.text)
for items in result:
  print items,':',result[items]



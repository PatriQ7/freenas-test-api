#!/usr/local/bin/python

import requests
import json

service = 'ssh'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "ssh_rootlogin": True,
          "ssh_compression": False
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/' + service + '/' 

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)

result = json.loads(r.text)
for items in result:
  print items,':',result[items]



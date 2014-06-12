#!/usr/local/bin/python

import requests
import json

service = 'nfs'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "nfs_srv_servers": 10,
          "nfs_srv_udp": True
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/' + service + '/' 

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)

result = json.loads(r.text)
for items in result:
  print items,':',result[items]



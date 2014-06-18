#!/usr/local/bin/python

import requests
import json

service = 'rsyncd'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "rsyncd_auxiliary": "",
          "rsyncd_port": 873
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/' + service + '/'

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)

result = json.loads(r.text)
for items in result:
  print items,':',result[items]



#!/usr/local/bin/python

import requests
import json

headers = {'Content-Type':'application/json'}
payload = {
          "ddns_provider": "dyndns@dyndns.org",
          "ddns_username": "admin"
}

r = requests.put('http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/dynamicdns/',auth=('root','patrick'),data=json.dumps(payload),headers=headers)
print r.status_code
result = json.loads(r.text)

for items in result:
  print items,':',result[items]



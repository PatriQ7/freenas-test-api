#!/usr/local/bin/python

import requests
import json

headers = {'Content-Type':'application/json'}

payload = {
          "ftp_timeout":"500",
          "ftp_clients":"10"
}
 
r = requests.put('http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/ftp/',auth=('root','patrick'),data=json.dumps(payload),headers=headers)
#r = requests.get('http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/ftp/',auth=('root','patrick'))
print r.text
result = json.loads(r.text)
for items in result:
  print items,':',result[items]



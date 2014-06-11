#!/usr/local/bin/python

import requests
import json

headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "ftp_client":10

}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/services/ftp/' 

r = requests.put(url,auth=auth,headers=headers,data=json.dumps(payload))
#r = requests.get(url,auth=auth)
print r.status_code
result = json.loads(r.text)
for items in result:
  print items,':',result[items]



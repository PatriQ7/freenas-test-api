#!/usr/local/bin/python

import requests
import json

service = 'settings'
headers = {'Content-Type':'application/json'}
auth = ('root','patrick')
payload = {
          "stg_timezone": "America/Los_Angeles",
          "stg_guiport": 80,
          "stg_guihttpsport": 443,
          "stg_guiprotocol": "http",
          "stg_guiv6address": "::",
          "stg_syslogserver": "",
          "stg_language": "en",
          "stg_directoryservice": "",
          "stg_guiaddress": "0.0.0.0",
          "stg_kbdmap": "",
          "id": 1
}
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/system/' + service + '/' 

r = requests.put(url, auth = auth, data = json.dumps(payload), headers = headers)

result = json.loads(r.text)
for items in result:
  print items,':',result[items]



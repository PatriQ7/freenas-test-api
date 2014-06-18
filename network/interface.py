#!/usr/local/bin/python

import requests
import json

service = 'interface'
url = 'http://freenas-test1.sjlab1.ixsystems.com/api/v1.0/network/' + service + '/'
auth = ('root','patrick')
headers = {'Content-Type':'application/json'}
payload = {
          "int_ipv4address": "192.168.3.20",
          "int_name": "ext",
          "int_v4netmaskbit": "24",
          "int_interface": "em0"
}

def interface_get():
  r = requests.get(url, auth = auth)
  result = json.loads(r.text)
  i = 0
  for i in range(0,len(result)):
    print '\n'
    for items in result[i]:
      print items+':', result[i][items]

def interface_post():
  r = requests.post(url, auth = auth, data = json.dumps(payload), headers = headers)
  result = json.loads(r.text)
  for items in result:
    print items+':', result[items]

def interface_put():
  id = raw_input('Input id:')+'/'
  r = requests.put(url+id, auth = auth, data = json.dumps(payload), headers = headers)
  result = json.loads(r.text)
  for items in result:
    print items+':', result[items]

def interface_delete():
  id = raw_input('Input id:')+'/'
  r = requests.delete(url+id, auth = auth)
  print r.status_code

while(1):
  method = raw_input('Input method:')
  if method == 'get':
    interface_get()
  elif method == 'post':
    interface_post()
  elif method == 'put':
    interface_put()
  elif method == 'delete':
    interface_delete()

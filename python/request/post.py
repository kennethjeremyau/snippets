#!/usr/bin/env python

import requests

req = requests.post('url', data=str({ 'key': 'value' }))
status = req.status_code
header_content = req.headers['header']
text = r.text
json = req.json()

#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests

r = requests.get('http://www.httpbin.org')
print(r.status_code)
print(r.headers)
print(r.text)
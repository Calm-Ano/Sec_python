# coding: utf-8

import requests

url = 'http://yahoo.co.jp'
response = requests.get(url)
print(response.text)
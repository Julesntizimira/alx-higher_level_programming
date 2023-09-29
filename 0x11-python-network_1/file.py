#!/usr/bin/python3
from urllib.request import urlopen
import requests

'''
with urlopen('http://google.com') as resp:
    header = resp.info()
    print(header['Content-Type'])






import shutil
import tempfile
import urllib.request

with urllib.request.urlopen('http://python.org/') as response:
    with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        shutil.copyfileobj(response, tmp_file)

with open(tmp_file.name) as html:
    h = html.read()
    print(h)
'''
payload = {'key1': 'value1', 'key2': 'value2'}

r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)

import urllib.request
import json


payload = {
    'key1': 'value1',
    'key2': 'value2'
}
url = 'http://httpbin.org/get?' + urllib.parse.urlencode(payload) 
print(url)
with urllib.request.urlopen(url) as f:
    r = json.loads(f.read().decode('utf-8'))
    # print(f.read().decode('utf-8'))
    print(r)
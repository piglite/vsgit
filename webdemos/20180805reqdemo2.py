import requests
import json

resp = requests.get('http://httpbin.org/stream/4',stream=True)
for line in resp.iter_lines():
    if line:
        print(json.loads(line))
        

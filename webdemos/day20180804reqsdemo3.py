import requests
from requests import Request
r = requests.get('https://vts.vipcode.com')
print(r.status_code)
r.encoding='utf-8'
print(r.url)
print(r.history)



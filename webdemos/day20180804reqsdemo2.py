import requests
r = requests.get('https://sports.sina.com.cn')
print(r.status_code)
print(r.headers['content-type'])
print('content:----->',r.content)
print('===============================================')
print(r.encoding)
r.encoding='utf-8'
print(r.encoding)
print('text----->',r.text)


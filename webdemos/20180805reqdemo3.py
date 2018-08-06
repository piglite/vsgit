import requests

url = "https://api.github.com/search/code?q=addClass+user:mozilla&page=1&per_page=4"
resp = requests.head(url)
print('响应头中的link：',resp.headers['link'])

        

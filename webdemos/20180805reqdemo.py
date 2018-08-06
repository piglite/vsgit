import requests
def myfunc(req,*args,**kwargs):
    print('请求路径：',req.url)
    print('请求状态码：',req.status_code)
    print('请求头：',req.headers)
    print('Content-Type:',req.headers['content-type'])
requests.get('http://www.douban.com',hooks={'response':myfunc})


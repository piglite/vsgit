import requests
from bs4 import BeautifulSoup
import json
from time import sleep
#构建要爬取的超链接集合
def get_urls(s,e):
    urls = []
    for x in range(s,e+1):
        urls.append('http://www.majortests.com/gre/wordlist_%s'%str(x).zfill(2))
    return urls
#从某一个超链接中获取HTML数据流
def get_res(url):
    html = requests.get(url)
    return html.text
#从某一个超链接中获取BeautifulSoup对象
def get_htmlobj(html):
    return BeautifulSoup(html)
#获取单词们
def get_words(htmlobj):
    words = {}
    for count,wordlist in enumerate(htmlobj.find_all(class_='wordlist')):
        title =  'Group %d'%(count + 1)
        new_words={}
        for entry in wordlist.find_all('tr'):
            new_words[entry.th.text] = entry.td.text
        words[title]=new_words
    return words
#获取单词们JSON字符串
def save_as_json(data,out_file):
    with open(out_file,'w') as writer:
        jsonobj = json.dumps(data)
        writer.write(jsonobj)
#开始爬取
def start(urls):
    words = {}
    for u in urls:
        k = u.split('/')[-1]
        print('now crawling %s'%k)
        words[k] = get_words(get_htmlobj(get_res(u)))
        print(words[k])
        sleep(5)
    save_as_json(words,'mywords.json')



start(get_urls(1,10))
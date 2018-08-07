from bs4 import BeautifulSoup
from os.path import join,dirname,abspath,pardir
p = join(dirname(dirname(__file__)),r'html\scrap_examp.html')
#print(p)
htmlObj =  BeautifulSoup(open(p))
print(htmlObj.body.find_previous_sibling)



        

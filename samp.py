from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
import requests
#----------------------------------------------------------------------------
url = "https://www.fleetstudio.com/"
#----------------------------------------------------------------------------
html_page = requests.get("file://G:/vs_code_projects/crawler/www_fleetstudio_com")
print("---[" + str(html_page.status_code)+"]------")
print(html_page.headers)
# bs = BeautifulSoup(html_page.text,'html.parser')
# print(bs.prettify())
# res = bs.find_all('loc')
# print(res)
# for i in res:
#     print(i,end="\n")
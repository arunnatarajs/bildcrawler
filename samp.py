import requests
import re
from urllib.parse import urljoin, urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.skcet.ac.in/")
soup = BeautifulSoup(html.read(), 'lxml')
links = []
for link in soup.find_all('a'):
    links.append(link.get('href'))

print(links[:])
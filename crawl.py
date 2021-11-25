import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from htmldownloader import htmldownloader
import os
# import lxml

visited_links = []

base_url = 'https://www.tutorialspoint.com/'
visited_links.append(base_url)

htmlpages = urlparse(base_url).netloc.replace('.','_')
if not os.path.isdir(os.getcwd() + '/' + htmlpages):
    os.mkdir(os.getcwd() + '/' + htmlpages)

filename = base_url[ base_url.find('.') + 1 : base_url.rfind('.') ]
filename = filename.replace('.','_').replace('/','_')+ '.txt'

main_html = requests.get(base_url).text

bs = BeautifulSoup(main_html,'lxml')    # print(main_html)  # print(bs)
links = bs.find_all(['a','link'])
# print(bs.prettify())

#opening file to write links
links_file = open(filename, 'w')

for link in links:
    
    link_to_be_added = urljoin(base_url,link['href'])

    if link_to_be_added not in visited_links:
        links_file.write(link_to_be_added+'\n')
        visited_links.append(link_to_be_added)

links_file.close()


read_links = open(filename,'r')

i = 1
for links in read_links:
    htmldownloader(base_url,links,str(i))
    print(links + '- - - - - html downloaded - - - - -')
    i+=1

read_links.close()
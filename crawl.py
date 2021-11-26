import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from htmldownloader import htmldownloader
import os
import re
import time
# import lxml

def crawling(url):
    # base_url = 'https://www.tutorialspoint.com/'
    # visited_links.append(base_url)

    # htmlpages = urlparse(url).netloc.replace('.','_')
    # if not os.path.isdir(os.getcwd() + '/' + htmlpages):
    #     os.mkdir(os.getcwd() + '/' + htmlpages)

    # filename = url[ url.find('.') + 1 : url.rfind('.') ]
    # filename = filename.replace('.','_').replace('/','_')+ '.txt'

    main_html = requests.get(url).text

    bs = BeautifulSoup(main_html,'html.parser')    # print(main_html)  # print(bs)
    links = bs.find_all('a')
    # print(bs.prettify())

    #opening file to write links
    links_file = open(filename+'.txt', 'a')

    for link in links:
        try:
            # print(link['href'])
            link_to_be_added = urljoin(url,link['href'])

            if link_to_be_added not in visited_links:
                links_file.write(link_to_be_added+'\n')
                visited_links.append(link_to_be_added)
        except:
            pass

    links_file.close()


    read_links = open(filename+'.txt','r')

    i = 1
    for links in read_links:
        # print(links)
        htmldownloader(url,links,str(i))
        # print(links + '- - - - - html downloaded - - - - -')
        i+=1

    read_links.close()


def crawl_starter(depth,link_itr):
    if depth==0:
        print("exit")
    else:
        print(visited_links[link_itr])
        crawling(visited_links[link_itr])
        crawl_starter(depth-1,link_itr+1)
        


start = time.time()

link_itr = 0
visited_links = []

url = "https://www.fleetstudio.com/"
depth = 5
visited_links.append(url)



filename = urlparse(url).netloc.replace('.','_')            # creating file name like www_google_com

if not os.path.isdir(os.getcwd() + '/' + filename):         # checking if already folder exists if not create it
    os.mkdir(os.getcwd() + '/' + filename)                  # creating folder with name www_google_com

file = open(filename+'.txt','w')                            # creating text file www_google_com.txt to store links
file.write(url+"\n")
file.close()

crawl_starter(depth,link_itr)                               # calling crawl_starter to start crawling by passing base url and depth


end = time.time()
print(end-start)
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from filename_generator import basefile, html_file_name
from htmldownloader import htmldownloader
import os
import time


def crawling(url):
    global crawl_id
    
    html_page = requests.get(url)
    
    print( "Crawl id : {:04d} ".format(crawl_id) + " Url : " + url + " Status Code : " + str(html_page.status_code), end =" ")
    if True:                                             # html_page.headers['Content-Type'] == 'text/html':
        
        bs = BeautifulSoup(html_page.text,'html.parser')
    
        if url not in downloaded_links:
            
            f_name = html_file_name(url)
            f = open(f_name, "w", encoding="utf-8")
            f.write(str(bs))
            f.close()

            print("Downloaded path : " + f_name+"\n")

            downloaded_links.append(url)
        
        links = bs.find_all('a')
        # print(bs.prettify())

        #opening file to write links
        links_file = open(filename+'.txt', 'a')

        for link in links:
        
            try:
                new_link = urljoin(url,link['href'])

                if new_link not in master_links and urlparse(base_url).netloc == urlparse(new_link).netloc:
                    links_file.write(new_link+'\n')
                    master_links.append(new_link)
        
            except:
                pass

        links_file.close()
        
        crawl_id+=1


    # read_links = open(filename+'.txt','r')

    i = 1
    for links in master_links:
        # print(links)
        if links not in downloaded_links:
            htmldownloader(url,links,str(i))
            # print(links + '- - - - - html downloaded - - - - -')
            i+=1
            downloaded_links.append(links)

    # read_links.close()


def crawl_starter(depth,link_itr):
    if depth==0:
        print("exit")
    else:
        # print(master_links[link_itr])
        crawling(master_links[link_itr])
        crawl_starter(depth-1,link_itr+1)
        

#------------------------------------------------------------------------------------------------------------------------------------------------#
start = time.time()

crawl_id = 1
master_links = []
downloaded_links = []

base_url = url = "https://www.tcs.com/"
depth = 5
master_links.append(url)

filename = basefile(url)                                        # creating file name like www_google_com
html_folder = os.getcwd() + '/' + filename

if not os.path.isdir(html_folder):                              # checking if already folder exists if not create it
    os.mkdir(html_folder)                                       # creating folder with name www_google_com

file = open(filename+'.txt','w')                                # creating text file www_google_com.txt to store links
file.write(url+"\n")
file.close()

crawl_starter(depth,0)                                          # calling crawl_starter to start crawling by passing base url and depth

end = time.time()
print(end-start)
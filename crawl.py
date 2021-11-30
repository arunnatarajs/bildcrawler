from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from filename_generator import basefile
from htmldownloader import htmldownloader,not_downloaded
from os import mkdir,getcwd,path
from time import time
from concurrent.futures import ThreadPoolExecutor
from url_filter import urlfilter
from csv import writer
import config

def crawling(url):
    global crawl_id
    
    html_page = get(url)
    
    print( "Crawl id : {:04d} ".format(crawl_id) + " Url : " + url + " Status Code : " + str(html_page.status_code), end =" ")
        
    bs = BeautifulSoup(html_page.text,'html.parser')         
        
    links = bs.find_all('a')
    

    #opening file to write links
    # links_file = open(filename+'.txt', 'a')

    with open(filename + '.csv', 'a', newline='') as file:
        writer_object = writer(file)
        for link in links:
            try:
                new_link = urljoin(url,link['href'])
                if urlfilter(new_link) and new_link not in master_links and urlparse(base_url).netloc == urlparse(new_link).netloc:
                    writer_object.writerow(["{:04d} ".format(crawl_id),new_link,"null","not downloaded",crawl_id])  
                    # links_file.write(new_link+'\t'+ 'depth: ' + str(crawl_id)+'\n')
                    master_links.append(new_link)
                    not_downloaded.append(new_link)
        
            except:
                pass

    file.close()

    # links_file.close()
        
    crawl_id+=1

    with ThreadPoolExecutor(max_workers = config.admin['thread_count']) as executor:
        executor.map(htmldownloader,not_downloaded)

def crawl_starter(depth,link_itr):
    if depth==0:
        print("exit")
    else:
        crawling(master_links[link_itr])
        crawl_starter(depth-1,link_itr+1)
    
    
        

#------------------------------------------------------------------------------------------------------------------------------------------------#

def main_crawl(url):
    
    start = time()
    global crawl_id, filename, base_url

    crawl_id = 1
    base_url = url
    
    master_links.append(url)
    not_downloaded.append(url)

    filename = basefile(url)                                     # creating file name like www_google_com
    html_folder = getcwd() + '/' + filename

    if not path.isdir(html_folder):                              # checking if already folder exists if not create it
        mkdir(html_folder)                                       # creating folder with name www_google_com

    # file = open(filename+'.txt','w')                             # creating text file www_google_com.txt to store links
    # file.write(url+"\n")
    # file.close()

    with open(filename + '.csv', 'w', newline='') as file:
        writer_object = writer(file)
        writer_object.writerow(["CRAWL ID","URL","RESPONSE CODE","DOWNLOADED PATH","DEPTH"])  
    file.close()

    crawl_starter(config.admin['depth_level'],0)                                       # calling crawl_starter to start crawling by passing base url and depth

    end = time()
    print(end-start)
    
    return "executed.............."


master_links = []
crawl_id =1

filename=""

# main_crawl("https://www.w3schools.com/default.asp")
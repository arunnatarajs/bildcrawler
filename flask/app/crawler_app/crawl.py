from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from os import mkdir, getcwd, path, listdir
# from time import time
from concurrent.futures import ThreadPoolExecutor
from app.crawler_app import csvgenerator, filename_generator,htmldownloader,url_filter,logger,config

def crawling(url):
    global link_id, crawl_id
    html_page = get(url, timeout=10)

    print("Crawl id : {:04d} ".format(crawl_id) + " Url : " + url + " Status Code : " + str(html_page.status_code),
          end=" ")

    bs = BeautifulSoup(html_page.text, 'html.parser')

    links = bs.find_all('a')

    for link in links:
        try:
            new_link = urljoin(url, link['href'])
            if url_filter.urlfilter(new_link) and new_link not in master_links and urlparse(base_url).netloc == urlparse(
                    new_link).netloc:
                link_id += 1
                htmldownloader.csv_list[new_link] = ["{:04d}".format(link_id), new_link, "null", "not downloaded", crawl_id]
                # links_file.write(new_link+'\t'+ 'depth: ' + str(crawl_id)+'\n')
                master_links.append(new_link)
        except Exception as e:
           logger.log_warning_writer(e)
            

    # print('\n no of links'+len(master_links))        
    crawl_id += 1

    with ThreadPoolExecutor(max_workers=config.admin['thread_count']) as executor:
        executor.map(htmldownloader.htmldownloader, master_links)


def crawl_starter(depth, link_itr):
    if depth == 0:
        print("exit")
        csvgenerator.csvgenerator(filename, htmldownloader.csv_list)
        # print(listdir(filename_generator.html_file_name("https://www.fleetstudio.com/")))

    else:
        crawling(master_links[link_itr])
        crawl_starter(depth - 1, link_itr + 1)


# ------------------------------------------------------------------------------------------------------------------------------------------------#

def main_crawl(url):
    
    global base_url, filename

    # start = time()

    base_url = url

    master_links.append(url)

    filename = filename_generator.basefile(url)  # creating file name like www_google_com
    html_folder = getcwd() + '/' + filename
    print(html_folder)

    if not path.isdir(html_folder):  # checking if already folder exists if not create it
        mkdir(html_folder)  # creating folder with name www_google_com

    htmldownloader.csv_list[url] = ["{:04d} ".format(0), url, "null", "not downloaded", 0]

    crawl_starter(config.admin['depth_level'],
                  0)  # calling crawl_starter to start crawling by passing base url and depth

    # end = time()
    # print(end - start)

    return "crawling executed.............."


master_links = []
base_url = ""
link_id = 0
crawl_id = 0

# main_crawl("https://www.apollohospitals.com/")

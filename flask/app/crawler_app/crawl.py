from requests import get
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
from app.crawler_app import csvgenerator,htmldownloader,url_filter,logger,config

def crawling(url):
    global link_id, crawl_id
    html_page = get(url, timeout=10)                                  #requests waits only for 10s 

    # print("Crawl id : {:04d} ".format(crawl_id) + " Url : " + url + " Status Code : " + str(html_page.status_code),
    #       end=" ")

    bs = BeautifulSoup(html_page.text, 'html.parser')                  #using BeautifulSoup html parsed

    links = bs.find_all('a')                                           #finding all anchor tag in the html page

    for link in links:
        try:
            new_link = urljoin(url, link['href'])                      #relative url is converted into absolute url
            if url_filter.urlfilter(new_link) and new_link not in master_links and urlparse(config.user['base_url']).netloc == urlparse(
                    new_link).netloc:                                                                                          #checking for valid link
                link_id += 1
                htmldownloader.csv_list[new_link] = ["{:04d}".format(link_id), new_link, "null", "not downloaded", crawl_id]  # adding url with link_id to list
                # links_file.write(new_link+'\t'+ 'depth: ' + str(crawl_id)+'\n')
                master_links.append(new_link)
        except Exception as e:
            pass
        #    logger.log_warning_writer(e)
            

    # print('\n no of links'+len(master_links))        
    crawl_id += 1

    with ThreadPoolExecutor(max_workers=config.admin['thread_count']) as executor:     #parallel programming implemented using ThreadPoolExecuor
        executor.map(htmldownloader.htmldownloader, master_links)                      #passing function and list of links to executor


def crawl_starter(depth, link_itr):
    if depth == 0:                                          #exits while depth becomes zero
        print("exit")                                       

    else:
        crawling(master_links[link_itr])                    #calling crawling function by passing a url to it to perform operation
        crawl_starter(depth - 1, link_itr + 1)              #decreasing depth by 1 and increasing link_itr by 1 and recursion is done here


# ------------------------------------------------------------------------------------------------------------------------------------------------#

def main_crawl(url,job_id,stage_id):
    

    config.user['base_url'] = url                           #setting base_url given by user
    config.user['job_id'] = job_id                          #setting job_id to user given job_id
    config.user['stage_id'] = stage_id                      #setting stage_id to user given stage_id

    master_links.append(url)

    htmldownloader.csv_list[url] = ["{:04d}".format(0), url, "null", "not downloaded", 0]

    crawl_starter(config.admin['depth_level'], 0)           #calling crawl_starter to start crawling by passing  depth


    return "crawling executed.............."


master_links = []
link_id = 0
crawl_id = 0

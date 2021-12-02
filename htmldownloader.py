from requests import get,exceptions
from bs4 import BeautifulSoup
from filename_generator import html_file_name

downloaded_links = []
csv_list = {}

def htmldownloader(url):
    
    if url not in downloaded_links:
        
        try:
            html_page = get(url,timeout=10)

            bs = BeautifulSoup(html_page.text,'html.parser')

            
        
            filename = html_file_name(url,csv_list[url][0])

            download_file = open(filename, "w", encoding="utf-8")
            download_file.write(str(bs))
            download_file.close()

            update = csv_list[url]
            update[2],update[3] = html_page.status_code,filename
            csv_list[url] = update
            
            downloaded_links.append(url)
            print("\nUrl : "+ url + " Status Code : " + str(html_page.status_code)+" Downloaded path : " + filename+"\n")
        except exceptions.ReadTimeout:
            update = csv_list[url]
            update[3] = "timeout"
            csv_list[url] = update

        except:
            pass
         
    else:
        pass
        # print("\n Already downloaded \n")




    
    
            

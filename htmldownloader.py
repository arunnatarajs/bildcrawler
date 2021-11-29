from requests import get
from bs4 import BeautifulSoup

from filename_generator import html_file_name

downloaded_links = []

def htmldownloader(url):
    
    # # print(parsed_url)
    # if parsed_url in base_url:          # and not (True in [i in url for i in ['.css','.ico','.php']]):
    #     # filename = url[ url.find('.') + 1 : url.rfind('.') ]
    #     # filename = filename.replace('.','_').replace('/','_')+ '.html'
    if url not in downloaded_links:
        downloaded_links.append(url)
        try:
            # main_html = urlopen(url)
            # read_file = main_html.read().decode("utf8")


            html_page = get(url)
            # print("\nUrl : "+ url + " Status Code : " + str(html_page.status_code), end =" ")
            bs = BeautifulSoup(html_page.text,'html.parser')
                # read_file_str = str(read_file)
                # outputfile = read_file_str.split('\\n')

        
                # print(filename)
            filename = html_file_name(url)
            download_file = open(filename, "w", encoding="utf-8")
            download_file.write(str(bs))
            download_file.close()
            print("\nUrl : "+ url + " Status Code : " + str(html_page.status_code)+" Downloaded path : " + filename+"\n")
        

            
        except:
            pass
    else:
        pass




    
    
            

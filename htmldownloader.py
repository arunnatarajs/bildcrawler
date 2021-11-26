import requests
from bs4 import BeautifulSoup

from filename_generator import html_file_name

def htmldownloader(base_url,url,i):
    
    # # print(parsed_url)
    # if parsed_url in base_url:          # and not (True in [i in url for i in ['.css','.ico','.php']]):
    #     # filename = url[ url.find('.') + 1 : url.rfind('.') ]
    #     # filename = filename.replace('.','_').replace('/','_')+ '.html'

    try:
        # main_html = urlopen(url)
        # read_file = main_html.read().decode("utf8")


        html_page = requests.get(url)
        print("---[" + str(html_page.status_code)+"]------")
        bs = BeautifulSoup(html_page.text,'html.parser')
            # read_file_str = str(read_file)
            # outputfile = read_file_str.split('\\n')

        
            # print(filename)
        download_file = open(html_file_name(url), "w", encoding="utf-8")
        download_file.write(str(bs))
        download_file.close()
        

            
    except:
        pass




    
    
            

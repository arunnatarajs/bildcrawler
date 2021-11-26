import os
from urllib.request import urlopen
from urllib.parse import urlparse
import re

def htmldownloader(base_url,url,i):
    parsed_url = urlparse(url).netloc
    # # print(parsed_url)
    # if parsed_url in base_url:          # and not (True in [i in url for i in ['.css','.ico','.php']]):
    #     # filename = url[ url.find('.') + 1 : url.rfind('.') ]
    #     # filename = filename.replace('.','_').replace('/','_')+ '.html'

    try:
        main_html = urlopen(url)
        read_file = main_html.read().decode("utf8")
            # read_file_str = str(read_file)
            # outputfile = read_file_str.split('\\n')

        parsed_url = parsed_url.replace('.','_')
        filename = re.sub(r'[^a-zA-Z0-9]','_',urlparse(url).path)
        filename = os.getcwd() +'/' + parsed_url + '/' + filename +'.html'
            # print(filename)
           

        download_file = open(filename,'w')

        download_file.write(read_file)
        download_file.close()

            
    except:
        pass
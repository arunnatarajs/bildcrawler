from urllib.request import urlopen
from urllib.parse import urlparse

def htmldownloader(base_url,url,i):
    
    parsed_url = urlparse(url).netloc
    if parsed_url in base_url and '.css' not in url:

        # filename = url[ url.find('.') + 1 : url.rfind('.') ]
        # filename = filename.replace('.','_').replace('/','_')+ '.html'
    
        main_html = urlopen(url)
        read_file = main_html.read()
        read_file_str = str(read_file)
        outputfile = read_file_str.split('\\n')

        parsed_url = parsed_url.replace('.','_')
        download_file = open(parsed_url + '/' + i +'.html','w')
        
        for line in outputfile:
            download_file.write(line+'\n')
        download_file.close()
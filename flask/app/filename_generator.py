from urllib.parse import urlparse
from os import getcwd
 
def basefile(url):
    filename = urlparse(url).netloc.replace('.','_') 
    return filename

def html_file_name(url,num):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace('.','_')
    filename = num
    filename = getcwd() +'/' + parsed_url + '/' + filename +'.html'
    return filename
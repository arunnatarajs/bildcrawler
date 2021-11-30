from urllib.parse import urlparse
from re import sub
from os import getcwd
 
def basefile(url):
    filename = urlparse(url).netloc.replace('.','_') 
    return filename

def html_file_name(url):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace('.','_')
    filename = sub(r'[^a-zA-Z0-9]','_',urlparse(url).path)
    filename = getcwd() +'/' + parsed_url + '/' + filename +'.html'
    return filename
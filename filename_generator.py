from urllib.parse import urlparse
import re
import os

def basefile(url):
    filename = urlparse(url).netloc.replace('.','_') 
    return filename

def html_file_name(url):
    parsed_url = urlparse(url).netloc
    parsed_url = parsed_url.replace('.','_')
    filename = re.sub(r'[^a-zA-Z0-9]','_',urlparse(url).path)
    filename = os.getcwd() +'/' + parsed_url + '/' + filename +'.html'
    return filename
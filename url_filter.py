from urllib.parse import urlparse

extensions = ['.pdf','.css','.xlxs','.doc','.jpg','.jpeg','.png','.json']
def urlfilter(url):
    parse_url = urlparse(url)
    if any(extension in parse_url.path for extension in extensions):
        return False
    return True
from urllib.parse import urlparse
from app.crawler_app import config

extensions = config.admin['extensions']


def urlfilter(url):
    parse_url = urlparse(url)
    if any(extension in parse_url.path for extension in extensions):
        return False
    return True

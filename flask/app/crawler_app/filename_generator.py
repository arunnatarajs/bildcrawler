from urllib.parse import urlparse


def basefile(url):
    filename = urlparse(url).netloc.replace('.', '_')
    return filename


def html_file_name(num):

    filename = num
    filename = filename + '.html'
    return filename

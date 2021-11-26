from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
#----------------------------------------------------------------------------
URL = "https://www.tutorialspoint.com/index.htm"
#----------------------------------------------------------------------------
soup = BeautifulSoup(urlopen(URL).read(), "html.parser")
f = open("samp.html", "w", encoding="utf-8")
f.write(str(soup.html))
f.close()

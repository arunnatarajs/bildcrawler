from requests import get
from bs4 import BeautifulSoup
from csv import writer

from filename_generator import basefile, html_file_name

downloaded_links = []
not_downloaded = []


def htmldownloader(url):
    
    if url not in downloaded_links:
        downloaded_links.append(url)
        not_downloaded.remove(url)
        try:
            
            html_page = get(url)

            bs = BeautifulSoup(html_page.text,'html.parser')
    
            filename = html_file_name(url)
            download_file = open(filename, "w", encoding="utf-8")
            download_file.write(str(bs))
            download_file.close()

            # fields = ['Name', 'Branch', 'Year', 'CGPA'] 

            # with open(basefile(url)+'.csv', 'a', newline='') as f_object:
            #     writer_object = writer(f_object)
            #     writer_object.writerow([url,html_page.status_code,filename])
            # f_object.close()
            print("\nUrl : "+ url + " Status Code : " + str(html_page.status_code)+" Downloaded path : " + filename+"\n")
         
        except:
            pass
    else:
        pass




    
    
            

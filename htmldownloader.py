from os import error
from requests import get
from bs4 import BeautifulSoup
from pandas import read_csv
from tempfile import NamedTemporaryFile
import shutil
import csv

from filename_generator import basefile, html_file_name
from samp import update_csv

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

            
            df = read_csv(basefile(url.strip())+".csv")
            df.loc[df["URL"]==url.strip(),['RESPONSE CODE','DOWNLOADED PATH']] = [200,filename]
            df.to_csv(basefile(url.strip())+".csv",index=False)

            # update_csv(url,html_page.status_code,filename)

            # filename = basefile(url)+'.csv'
            # tempfile = NamedTemporaryFile(mode='w', delete=False)
            # fields = ["CRAWL ID","URL","RESPONSE CODE","DOWNLOADED PATH","DEPTH"]
            # with open(basefile(url)+'.csv', 'r') as csvfile, tempfile:
            #     reader = csv.DictReader(csvfile, fieldnames=fields)
            #     writer = csv.DictWriter(tempfile, fieldnames=fields)
            #     for row in reader:
            #         if row['URL'] == url:
            #             print('updating row', row['URL'])
            #             row['RESPONSE CODE'], row['DOWNLOADED PATH'] = html_page.status_code, filename
            #         row = {'CRAWL ID': row['CRAWL ID'], 'URL': row['URL'], 'RESPONSE CODE': row['RESPONSE CODE'], 'DOWNLOADED PATH': row['DOWNLOADED PATH'], 'DEPTH': row['DEPTH']}
            #         writer.writerow(row)
            # shutil.move(tempfile.name, filename)

            # print("\nUrl : "+ url + " Status Code : " + str(html_page.status_code)+" Downloaded path : " + filename+"\n")
         
        except error:

            print(error)
    else:
        pass




    
    
            

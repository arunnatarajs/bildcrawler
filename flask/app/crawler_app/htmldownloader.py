from requests import get, exceptions
from bs4 import BeautifulSoup
from app.crawler_app import filename_generator,logger

downloaded_links = []
csv_list = {}


def htmldownloader(url):
    if url not in downloaded_links:

        try:
            html_page = get(url, timeout=10)

            bs = BeautifulSoup(html_page.text, 'html.parser')

            filename = filename_generator.html_file_name(url, csv_list[url][0])

            download_file = open(filename, "w", encoding="utf-8")
            download_file.write(str(bs))
            download_file.close()

            update = csv_list[url]
            update[2], update[3] = html_page.status_code, filename
            csv_list[url] = update

            downloaded_links.append(url)
            logger.log_info_writer("Url : " + url + " Status Code : " + str(
                html_page.status_code) + " Downloaded path : " + filename)
        except exceptions.ReadTimeout as e:
            logger.log_error_writer(url +" "+str(e))
            update = csv_list[url]
            update[3] = "timeout"
            csv_list[url] = update

        except Exception as e:
            logger.log_error_writer(url+" "+str(e))

    else:
        pass
        # print("\n Already downloaded \n")
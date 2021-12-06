from app import app
from app.crawler_app import crawl
from flask import request

@app.route("/")
def hello_world():
    return "Welcome to crawler"


@app.route("/<path:url>")
def crawler(url):
    print(url)
    return crawl.main_crawl(url)
    # return "hello"

# @app.route("/crawler",methods = ["POST"])
# def crawler():
#     url = request.json["url"]
#     print(url)
#     return crawl.main_crawl(url)
#     # return "hello"
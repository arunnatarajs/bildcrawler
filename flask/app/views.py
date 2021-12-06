from app import app
from app.crawler_app import crawl
from flask import request

@app.route("/")
def hello_world():
    return "Welcome to crawler"


# @app.route("/<path:url>")
# def crawler(url):
#     print(url)
#     return crawl.main_crawl(url)
#     # return "hello"

@app.route("/crawler",methods = ["POST"])
def crawler():
    if request.args:
        args = request.args
        url = args.get("url")
        job_id = args.get("jobId")
        stage_id = args.get("stageId")
        print(url,job_id,stage_id,sep="\n")
        return crawl.main_crawl(url,job_id,stage_id)
        return "hello"
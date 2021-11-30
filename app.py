from flask import Flask

from crawl import main_crawl

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Welcome to crawler"

@app.route("/<path:url>")

def crawler(url):

    return (main_crawl(url))
    

if __name__ == "__main__":
    app.run(debug=True)
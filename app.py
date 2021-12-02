from flask import Flask

from crawl import main_crawl

import os
from flask import send_from_directory

app = Flask(__name__)




@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route("/")
def hello_world():
    return "Welcome to crawler"

@app.route("/<path:url>")
def crawler(url):
    print(url)
    
    return (main_crawl(url))
    
    

if __name__ == "__main__":
    app.run(debug=True)
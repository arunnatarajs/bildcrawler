from app import app
from app import app

@app.route("/")
def hello_world():
    return "Welcome to crawler"

@app.route("/<path:url>")
def crawler(url):
    print(url)
    
    return "hello"

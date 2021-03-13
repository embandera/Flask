#https://code.visualstudio.com/docs/python/tutorial-flask#_go-to-definition-and-peek-definition-commands
 
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        
    )
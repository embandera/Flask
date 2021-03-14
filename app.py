# from datetime import datetime
from flask import Flask, render_template
# from . import app

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name=None):
    return render_template(
        "hello_there.html",
        name=name)

# @app.route("/api/data")
# def get_data():
#     return app.send_static_file("data.json")

# https://macfire.github.io/devops16/html/devops16_6_deploy_flask_app_w_git.html
# https://dev.to/lordofdexterity/deploying-flask-app-on-heroku-using-github-50nh
# https://www.freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221/

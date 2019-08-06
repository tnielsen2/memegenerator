from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/dual")
def dual():
    return "This is the page for dual layer memes"

@app.route("/single")
def single():
    return "This is the page for single layer memes"

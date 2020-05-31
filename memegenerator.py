from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/dual")
def dual():
    backgrounds = os.listdir('./backgrounds/')
    foregrounds = os.listdir('./foregrounds/')
    return render_template('dual.html', backgrounds=backgrounds, foregrounds=foregrounds)

@app.route("/dualresult")
def dualresult():
    if request.method == 'POST':
        result = request.form
        return render_template("dualresult.html", result=result)

@app.route("/single")
def single():
    return "This is the page for single layer memes"

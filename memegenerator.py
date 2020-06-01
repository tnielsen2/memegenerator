from flask import Flask, render_template, request
import os
import dual_gen

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route("/dual", methods=['POST', 'GET'])
def dual():
    if request.method == 'GET':
        backgrounds = os.listdir('./backgrounds/')
        foregrounds = os.listdir('./foregrounds/')
        return render_template('dual.html', backgrounds=backgrounds, foregrounds=foregrounds)
    elif request.method == 'POST':
        return dualresult()

@app.route("/testform", methods=['POST', 'GET'])
def testform():
    if request.method == 'GET':
        backgrounds = os.listdir('./backgrounds/')
        foregrounds = os.listdir('./foregrounds/')
        return render_template('testform.html', backgrounds=backgrounds, foregrounds=foregrounds)
    elif request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        return data


@app.route("/dualresult")
def dualresult():
    if request.method == 'POST':
        result = request.form
        return render_template("dualresult.html", result=result)

@app.route("/single")
def single():
    return "This is the page for single layer memes"

from flask import Flask, render_template, request, redirect
# Form imports
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField
from wtforms.validators import DataRequired
from werkzeug.utils import secure_filename

import os

SECRET_KEY = os.urandom(32)

# Classes
class MyForm(FlaskForm):
    name = StringField('Meme Text:', validators=[DataRequired()])

class UploadForm(FlaskForm):
    upload = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ])

# Functions
def allowed_image(filename):

    # We only want files with a . in the filename
    if not "." in filename:
        return False

    # Split the extension from the filename
    ext = filename.rsplit(".", 1)[1]

    # Check if the extension is in ALLOWED_IMAGE_EXTENSIONS
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False


# Flask
app = Flask(__name__)

### App configuration (https://flask.palletsprojects.com/en/1.1.x/config/)
# Secret key randomly generated every time Flask starts
app.config['SECRET_KEY'] = SECRET_KEY
## Image upload settings
# Default app upload folder
app.config["IMAGE_UPLOADS"] = './backgrounds'
# Maximum file size
app.config['MAX_CONTENT_PATH'] = '20000000'
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024


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

@app.route("/dualresult")
def dualresult():
    if request.method == 'POST':
        result = request.form
        return render_template("dualresult.html", result=result)

@app.route("/single")
def single():
    return "This is the page for single layer memes"

@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

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

# https://pythonise.com/series/learning-flask/flask-uploading-files
@app.route("/upload-image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                print("No filename")
                return redirect(request.url)
            if allowed_image(image.filename):
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                print("Image saved")
                return redirect(request.url)
            else:
                print("That file extension is not allowed")
                return redirect(request.url)
    return render_template("upload-image.html")
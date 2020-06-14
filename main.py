#simple backend using python flask

from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/upload')

def upload():
    return render_template('image_load.html')

app.run(debug=True)


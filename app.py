import os
from yatta.yatta import senti
from flask import Flask, flash, request, redirect
from flask import send_file, render_template

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# ADD a png,jpg,jpeg limit!

app = Flask(__name__)
app.static_folder = 'static'

app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024 # 8mb


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            # Sentification!
            return send_file(senti(file), as_attachment=True, download_name='result.gif', mimetype='image/gif')
    
    return render_template('index.html')

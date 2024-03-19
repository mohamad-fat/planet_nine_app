from flask import Flask, flash, render_template, request, redirect, url_for
import urllib.request
import os
from waitress import serve
from werkzeug.utils import secure_filename

from model import predict_object

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = 'cairocoders-ednalan'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENTIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENTIONS


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No image selected for uploading')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        flash('Image successfully uploaded and displayed above')
        
        data = predict_object(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction = data[0][0]

        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        return render_template('index.html', filename=filename, prediction=prediction, labels=labels, values=values)
    else:
        flash('Alowed image types are - png, jpg, jpeg, gif')
        return redirect(request.url)
    
@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename, code=301))

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000)
    serve(app, host='0.0.0.0', port=8000)
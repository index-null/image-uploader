from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
from config import Config
import os
from models.image_handler import ImageChecker, ImageSaver

app = Flask(__name__)
app.config.from_object(Config)

# 确保上传文件夹存在
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload():
    is_valid, error = ImageChecker.validate_file(request)
    if not is_valid:
        flash(error)
        return redirect(request.url)
    
    file = request.files['file']
    filename = ImageSaver.save_file(file, app.config['UPLOAD_FOLDER'])
    return redirect(url_for('uploaded_file', filename=filename))

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return render_template('uploaded.html', file_name=filename)

if __name__ == '__main__':
    app.run(debug=True)
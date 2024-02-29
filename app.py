from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Configure upload folder path
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp4', 'webm', 'ogg', 'wmv'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # Handle POST Request
    if request.method == 'POST':
        if 'video' not in request.files:
            return redirect(request.url)

        uploaded_file = request.files['video']
                
        if uploaded_file.filename == '':
            return redirect(request.url)

        if uploaded_file and allowed_file(uploaded_file.filename):
            filename = secure_filename(uploaded_file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            uploaded_file.save(filepath)

            return render_template('index.html', saved_path=filepath, success=True) 
        else:
            return render_template('index.html')
        
    # Handle GET Request    
    if request.method == 'GET':
        return render_template('index.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(port=3000, debug=True)

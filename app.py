import os

from flask import Flask, render_template, request, make_response
from werkzeug.utils import secure_filename

from models import random_choice

app = Flask(__name__)

UPLOAD_FOLDER = './data'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        upload_img= request.files['file']
        filename = secure_filename(upload_img.filename)
        upload_img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        img_url = './data/' + filename
        result = random_choice(img_url)
        output = make_response()
        output.data = result.getvalue().encode("utf_8_sig")
        output.headers["Content-type"] = "text/csv"
        if not upload_img:
            return render_template('index.html')
        else:
            return output
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
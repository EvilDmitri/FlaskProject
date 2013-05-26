import os
from werkzeug import security
from flask import Flask, Request, Response, render_template, request, redirect, url_for


UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'py'])

application = app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/", methods=['GET', 'POST'])
def first():
    if request.method == 'POST':

        file_func = request.files['file']
        if file_func and allowed_file(file_func.filename):
            filename = file_func.filename
            file_func.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

            with(open(os.path.join(app.config['UPLOAD_FOLDER'],filename))) as f:
                func_body = f.readlines()
                return render_template('first.html', func=func_body)
        else:
            func_body = 'Only .py and .txt files allowed'
            return render_template('first.html', func=func_body)

    return render_template('first.html', func='')


@app.route('/result', methods=['GET', 'POST'])
def result():
    return 'Under construction'


from flask import send_from_directory
# Show file content
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

@app.route('/files')
def files():
    files = os.listdir('uploads')
    return render_template('file_list.html', files=files)



@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hellohei():
    return "Hello World!"

@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route("/first")
def first():
    return render_template('first.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0')

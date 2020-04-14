from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/user/<username>')
def index(username):
    return render_template('index.html', username=username)

@app.route('/')
def hello_world():
    render_template
    return 'Hello, World!'

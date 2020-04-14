from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/register')
def index():
    return render_template('/auth/register.html')

@app.route('/')
def hello_world():
    return render_template('index.html')

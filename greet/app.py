from flask import Flask

app = Flask(__name__)

@app.route('/welcome')
def get_welcome():
    return '<h1>Welcome</h1>'

@app.route('/welcome/home')
def get_welcome_home():
    return '<h1>Welcome Home</h1>'


@app.route('/welcome/back')
def get_welcome_back():
    return '<h1>Welcome Back</h1>'
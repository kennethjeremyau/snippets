from flask import Flask
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def send():
    return send_from_directory('html', 'hi.html')

@app.route('/hello')
def hello():
    return 'hi'

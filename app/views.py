from app import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "This webhook page!"

@app.route('/project', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        data = request.json
        print data
        return 'ok'
    else:
        return 'not get method'
from app import app
from flask import request
import json

@app.route('/')
@app.route('/index')
def index():
    return "This webhook page!"

@app.route('/project', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        project_name = data['repository']['name']
        print project_name
        print json.dumps(data, sort_keys=True, indent=2)
        return 'ok'
    else:
        return 'not get method'

from app import app
from flask import request
import logging
import os

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='/var/log/webhook.log',
                filemode='w')

@app.route('/')
@app.route('/index')
def index():
    return "This webhook page!"


@app.route('/project', methods=['POST','GET'])
def webhook():
    if request.method == 'POST':
        data = request.get_json()
        project_name = data['repository']['name']
        #print project_name
        #print json.dumps(data, sort_keys=True, indent=2)
        if project_name and isinstance(project_name, str):
            command = "python /usr/local/bin/deploy-code.py %s pull && python /usr/local/bin/deploy-code.py %s sync" % (project_name,project_name)
            os.system(command)
            logging.info(command)
        return 'ok'
    else:
        return 'not get method'

import json
from client import *
from flask import render_template
from flask import request
from flask import Flask


app = Flask(__name__)


@app.route('/index')
def mainpage():
    return render_template('index.html')


@app.route('/amqp', methods=['POST'])
def amqp():
    msg = json.dumps(request.form.to_dict())
    j = json.loads(msg)

    send_msg = j['msg']
    number_sent = len(send_msg.split(','))
    print(send_msg) # send this message through protocol
    print(number_sent)

    result = protocol_test(send_msg)
    print(result)
    return str(result)



if __name__ == "__main__":
    app.run()

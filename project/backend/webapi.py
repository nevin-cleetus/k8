import os
import socket
import logging
import datetime
from logging.handlers import RotatingFileHandler


from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello():
    # hostname = socket.gethostbyaddr(request.remote_addr)
    hostname = socket.gethostname()
    # print(hostname)
    # print(request.remote_addr)
    # return request.remote_addr
    # str(datetime.datetime.now())

    root = os.path.dirname(os.path.abspath(__file__))
    logdir = os.path.join(root, 'logs')
    log_file = os.path.join(logdir, str(datetime.datetime.now())+'_app.log')
    handler = logging.FileHandler(log_file)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)
    app.logger.warning('Backend API called ...' + str(datetime.datetime.now()))
    return hostname

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


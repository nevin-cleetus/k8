import os
import sys
import requests
import socket
from flask import Flask,render_template,request
from dotenv import load_dotenv, find_dotenv

app = Flask(__name__)

@app.route('/')
def index():
    webapiHostName = get_webapi_hostname()
    hostName = get_hostname()

    hostName = 'Frontend hostname... "{0}" Backend hostname:... "{1}"'.format(hostName, webapiHostName)
    return render_template('index.html',hostName = hostName)


def get_hostname():
    return socket.gethostname();

def get_webapi_hostname():
    # the web container MUST be run with --link <appName>:helloapp
    # link_alias = 'helloapp'

    # Load the environment variables from the .env file.
    # They will be overwritten if environment vars are set
    load_dotenv(find_dotenv())
    url = os.environ.get("APPURL")

    # Request data from the app container


#!/bin/python3

import os
from flask import Flask
from flask import send_from_directory

app = Flask(__name__)



@app.route('/')
def main_page():
    # Smart code stuff here
    return '<link rel="shortcut icon" href="{{ url_for(static, filename=favicon.ico) }}">'

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

#!/bin/python3

from flask import Flask
app = Flask(__name__)



@app.route('/')
def main_page():
    # Smart code stuff here
    return 'good morning'

@app.route('/favicon.ico')
def favicon():
    return 'a'

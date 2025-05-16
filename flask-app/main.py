#!/usr/bin/env python

import flask
import socket

hostname = socket.gethostname()

app = flask.Flask(__name__)

@app.route('/')
def index():
    return f"This is {hostname} running Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

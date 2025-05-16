#!/usr/bin/env python

import flask
import socket
import os
import redis

hostname = socket.gethostname()
redis_host = os.getenv('REDIS_HOST', 'localhost')
redis_port = os.getenv('REDIS_PORT', 6379)
r = redis.Redis(host=redis_host, port=redis_port)
# r.set("key", "value")
# print(r.get("key"))

app = flask.Flask(__name__)

@app.route('/')
def index():
    if not r.exists("hit_counter"):
        r.set("hit_counter", 0)
    hit_count = r.get("hit_counter")
    hit_count += 1
    r.set("hit_counter", hit_count)
    return f"This is {hostname} running Flask. Hits: {hit_count}!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

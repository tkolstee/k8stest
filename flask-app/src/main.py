#!/usr/bin/env python

import flask
import socket
import os
import redis
import pika


config = {}
for var in ['MQ_SERVER', 'MQ_USER', 'MQ_PASS', 'REDIS_HOST', 'REDIS_PORT']:
	val = os.getenv(var)
	if val is None:
		print(f"Environment variable {var} not set.")
		exit(1)
	else:
		config[var] = val

hostname = socket.gethostname()
creds = pika.PlainCredentials(username=config['MQ_USER'], password=config['MQ_PASS'])
conn_params = pika.ConnectionParameters(config['MQ_SERVER'], credentials=creds)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()
channel.queue_declare(queue='hello')


app = flask.Flask(__name__)

@app.route('/')
def index():
	r = redis.Redis(host=config['REDIS_HOST'], port=config['REDIS_PORT'])
	if not r.exists("hit_counter"):
		r.set("hit_counter", 0)
	hit_count = int(r.get("hit_counter")) + 1
	r.set("hit_counter", hit_count)
	response = f"This is {hostname} running Flask. Hits: {str(hit_count)}!"
	channel.basic_publish(exchange='', routing_key='hello', body=response)
	return response

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)



import pika
import os
import socket
import time

config = {}
for var in ['MQ_SERVER', 'MQ_USER', 'MQ_PASS']:
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

for _ in range(5):
	channel.basic_publish(exchange='', routing_key='hello', body=hostname)
	print(f" [x] Sent '{hostname}'")
	time.sleep(5)



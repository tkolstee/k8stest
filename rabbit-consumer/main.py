import pika
import os

config = {}
for var in ['MQ_SERVER', 'MQ_USER', 'MQ_PASS']:
	val = os.getenv(var)
	if val is None:
		print(f"Environment variable {var} not set.")
		exit(1)
	else:
		config[var] = val

def callback(ch, method, properties, body):
	print(f" [x] Received {str(body)}")

creds = pika.PlainCredentials(username=config['MQ_USER'], password=config['MQ_PASS'])
conn_params = pika.ConnectionParameters(config['MQ_SERVER'], credentials=creds)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_consume(
	queue='hello',
	auto_ack=True,
	on_message_callback=callback
)
print(' [*] Waiting for messages. To exit press CTRL+C.')
try:
	channel.start_consuming()
except KeyboardInterrupt:
	print('Interrupted.')
finally:
	connection.close()
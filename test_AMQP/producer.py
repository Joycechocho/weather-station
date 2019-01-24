# Modify CONFIG ENV FILE --IP ADDRESS
# Change CONFIG FILE -- LOGIN USER


import pika
import socket
from subprocess import call
import threading
import time

def rabbitmq_service():
    call(["rabbitmq-server"])

t = threading.Thread(name='start_Rabbitmq_Broker', target=rabbitmq_service)
t.start()

#my_ip = socket.gethostbyname(socket.gethostname())

time.sleep(5)
# Establish connection to a message broker on a local machine
# If need to connect to a different machine, replace 'localhost' with the name or ip address
credentials = pika.PlainCredentials('shuting', '8281887')
connection = pika.BlockingConnection(pika.ConnectionParameters(host='10.201.9.166',
                                                               port=5672,
                                                               virtual_host='/',
                                                               credentials=credentials))
# host=my_ip, port=9888
channel = connection.channel()

# Fair dispatch
channel.basic_qos(prefetch_count=1)

# Create a recipient queue
channel.queue_declare(queue='hello')

# A message needs to go through an exchange to be on the queue
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')

print("[x] Sent 'Hello World'")

connection.close()


import pika
from subprocess import call
import time
import threading
import socket
import websocket


global n
n = 0


def rabbitmq_service():
    call(["rabbitmq-server"])


#host_ip = socket.gethostbyname(socket.gethostname())
credentials = pika.PlainCredentials('shuting', '8281887')


def rabbitmq_service():
    call(["sudo", "rabbitmq-server"])


def start_amqp_test():
    t = threading.Thread(target=rabbitmq_service)
    t.start()
    time.sleep(20)
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="10.201.26.213",
                                                                   port=5672,
                                                                   virtual_host='/',
                                                                   credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_request, queue='rpc_queue')

    print('[AMQP test] Server started.')
    channel.start_consuming()
    print('finished')
    connection.close()
    time.sleep(2)
    call(["sudo", "rabbitmqctl", "shutdown"])
    websocket.start_websocket_test()


def on_request(ch, method, props, body):
    global n
    n += 1
    # Print out received msg
    print('[AMQP test] Message received: '+ str(body))
    print('[AMQP test] Echoing received message back...')
    ch.basic_publish(exchange='',
                     routing_key=props.reply_to,
                     properties=pika.BasicProperties(correlation_id=props.correlation_id),
                     body=body)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    if n == 3:
        n = 0
        print('[AMQP test] Shutdown server')
        ch.stop_consuming()

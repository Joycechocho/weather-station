import pika
import uuid
import time

credentials = pika.PlainCredentials('shuting', '8281887')

class AMQPClient(object):
    def __init__(self):
        self.response = None
        self.ms = 0
        self.connection =pika.BlockingConnection(pika.ConnectionParameters(host='10.201.9.97',
                                                                           port=5672,
                                                                           virtual_host='/',
                                                                           credentials=credentials))
        self.channel = self.connection.channel()
        self.result = self.channel.queue_declare(exclusive=True)
        self.callback_queue = self.result.method.queue
        self.channel.basic_consume(self.on_response, no_ack=True, queue=self.callback_queue)

    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.ms = int(round(time.time()*1000)) - self.ms
            length = len(body.decode().split(','))
            self.response = [self.ms, length]

    def send_msg(self, msg):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        self.ms = int(round(time.time()*1000))
        self.channel.basic_publish(exchange='',
                                   routing_key='rpc_queue',
                                   properties=pika.BasicProperties(
                                    reply_to = self.callback_queue,
                                    correlation_id = self.corr_id),
                                   body=msg)
        while self.response is None:
            self.connection.process_data_events()
        return self.response

a = AMQPClient()
# the return value rc is a list that contains the time it took and the length of the msg:
# rc = [time, length] eg.: rc = [44, 3] ---it took 44ms, received 3 numbers
rc = a.send_msg("22,23,23,42,33")
print(rc)

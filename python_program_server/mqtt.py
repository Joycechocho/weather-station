import paho.mqtt.client as mqtt
import amqp
import threading
from subprocess import call
import time

global n
n = 0

def start_mosquitto():
    call(["mosquitto"])


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("topic/incoming")


def on_message(client, userdata, msg):
    global n
    n += 1
    message = msg.payload.decode()
    print('received: '+message)
    time.sleep(4)
    client.publish("topic/out", message)
    if n == 3:
        time.sleep(8)
        n = 0
        client.disconnect()


def on_disconnect(client, userdata, flags):
    call(["killall", "mosquitto"])


def start_mqtt_test():
    t = threading.Thread(target=start_mosquitto)
    t.start()
    time.sleep(3)
    client = mqtt.Client()
    client.connect('10.201.26.213', 1883, 60)
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.loop_forever()
    amqp.start_amqp_test()

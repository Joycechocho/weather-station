import mqtt_publisher as mqtt
import amqp_client as amqp
import coap_client as coap
import time
import asyncio

def protocol_test(msg):
    result_ms = []
    result_number = []
    time.sleep(6)
    print('[mqtt] Start mqtt test...')
    mqtt_instance = mqtt.MQTTClient()
    for x in range(0, 3):
        print('[mqtt] Publishing for the '+str(x+1)+'th time')
        rc = mqtt_instance.publish("topic/incoming", msg)
        print('[mqtt] Received')
        result_ms.append(rc[0])
        result_number.append(rc[1])
    print('[mqtt] Disconnecting...')
    mqtt_instance.disconnect()
    mqtt_ms = sum(result_ms)/len(result_ms)
    mqtt_num = sum(result_number) / len(result_number)
    result_number.clear()
    result_ms.clear()
    time.sleep(24)
    print('[amqp] Start amqp test')
    amqp_instance = amqp.AMQPClient()
    for x in range (0, 3):
        print('[amqp] Sending the '+str(x+1)+'th message')
        rc = amqp_instance.send_msg(msg)
        print('[amqp] Received')
        result_ms.append(rc[0])
        result_number.append(rc[1])
    print('[amqp] Disconnecting...')
    amqp_instance.disconnect()
    amqp_ms = sum(result_ms)/len(result_ms)
    amqp_num = sum(result_number) / len(result_number)
    result_ms.clear()
    result_number.clear()
    time.sleep(6)
    print('[coap] Start coap test')
    coap_instance = coap.COAPClient()
    for x in range(0, 3):
        print('[coap] Sending the '+str(x+1)+'th PUT message')
        asyncio.get_event_loop().run_until_complete(coap_instance.put(msg))
        print('[coap] Received')
        rc = coap_instance.get_result()
        result_ms.append(rc[0])
        result_number.append(rc[1])
    print('[coap] Coap test completed')
    coap_ms = sum(result_ms)/len(result_ms)
    coap_num = sum(result_number)/len(result_number)

    return [mqtt_ms-4000, mqtt_num, amqp_ms, amqp_num, coap_ms, coap_num]



# r = protocol_test("22,2,33,24,33,23,23,23,23,23,23,23,23,23,23,23,23")
# print(r)

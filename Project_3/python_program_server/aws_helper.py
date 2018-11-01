'''
/*
 * Copyright 2010-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import logging
import time


# Custom MQTT message callback
def custom_callback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")


class AWSIoTHandler(object):

    def __init__(self, args=None):
        self.host = args.host
        self.root_CA_path = args.rootCAPath
        self.certificate_path = args.certificatePath
        self.private_key_path = args.privateKeyPath
        self.use_websocket = args.useWebsocket
        self.client_id = args.clientId
        self.topic = args.topic
        self.myAWSIoTMQTTClient = None
        self.configure_client()

    def configure_client(self):
        if self.use_websocket and self.certificate_path and self.private_key_path:
            print('X.509 cert authentication and WebSocket are mutual exclusive. Please pick one.')
            exit(2)

        if not self.use_websocket and (not self.certificate_path or not self.private_key_path):
            print('Missing credentials for authentication.')
            exit(2)

        # Configure logging
        logger = logging.getLogger("AWSIoTPythonSDK.core")
        logger.setLevel(logging.DEBUG)
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Init AWSIoTMQTTClient
        if self.use_websocket:
            self.myAWSIoTMQTTClient = AWSIoTMQTTClient(self.client_id, useWebsocket=True)
            self.myAWSIoTMQTTClient.configureEndpoint(self.host, 443)
            self.myAWSIoTMQTTClient.configureCredentials(self.root_CA_path)
        else:
            self.myAWSIoTMQTTClient = AWSIoTMQTTClient(self.client_id)
            self.myAWSIoTMQTTClient.configureEndpoint(self.host, 8883)
            self.myAWSIoTMQTTClient.configureCredentials(self.root_CA_path, self.private_key_path, self.certificate_path)

        # AWSIoTMQTTClient connection configuration
        self.myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
        self.myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
        self.myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
        self.myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
        self.myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

        # Connect and subscribe to AWS IoT
        self.myAWSIoTMQTTClient.connect()
        self.myAWSIoTMQTTClient.subscribe(self.topic, 1, custom_callback)
        time.sleep(2)
        print('AWS configuration complete.')

    def publish(self, message):
        self.myAWSIoTMQTTClient.publish(self.topic, message, 1)


# # Publish to the same topic in a loop forever
# loopCount = 0
# while True:
#     myAWSIoTMQTTClient.publish(topic, "New Message " + str(loopCount), 1)
#     loopCount += 1
#     time.sleep(1)

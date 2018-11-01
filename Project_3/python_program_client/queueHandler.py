# import boto3
# import json
# import time
# from credentials import AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY
#
# message_bodies = []
#
# # Get the service resource
# sqs = boto3.resource(
#     'sqs',
#     aws_access_key_id=AWS_ACCESS_KEY_ID,
#     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
#     region_name='us-west-2')
#
# # Get the queue
# queue = sqs.get_queue_by_name(QueueName='Weather')
#
# while True:
#     for message in queue.receive_messages(MaxNumberOfMessages=10):
#
#         message_bodies.append(message.body)
#         print(message.body)
#         #message.delete()
#


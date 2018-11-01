
import boto3

sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='testQueue.fifo')
client = boto3.client('sqs')


def lambda_handler(event, context):
    # passing msg to SQS
    response = client.get_queue_attributes(
        QueueUrl='https://sqs.us-west-2.amazonaws.com/838927694135/testQueue.fifo',
        AttributeNames=['ApproximateNumberOfMessages']
    )
    if int(response['Attributes']['ApproximateNumberOfMessages']) >= 15:
        delete_1_message(queue)
    write2sqs(queue, event)


def write2sqs(queue, msg):
    print(msg)
    response = queue.send_message(
        MessageAttributes={
            'Current_temperature': {
                'DataType': 'Number',
                'StringValue': str(msg['current_temperature'])
            },
            'Current_humidity': {
                'DataType': 'Number',
                'StringValue': str(msg['current_humidity'])
            },
            'Average_temperature': {
                'DataType': 'Number',
                'StringValue': str(msg['average_temperature'])
            },
            'Average_humidity': {
                'DataType': 'Number',
                'StringValue': str(msg['average_humidity'])
            },
            'High_temperature': {
                'DataType': 'Number',
                'StringValue': str(msg['high_temperature'])
            },
            'High_humidity': {
                'DataType': 'Number',
                'StringValue': str(msg['high_humidity'])
            },
            'Low_temperature': {
                'DataType': 'Number',
                'StringValue': str(msg['low_temperature'])
            },
            'Low_humidity': {
                'DataType': 'Number',
                'StringValue': str(msg['low_humidity'])
            },
        },
        MessageBody=('1'),
        MessageDeduplicationId=str(msg['time_stamp']),
        MessageGroupId='string'
    )
    print(response.get('Failed'))
    print(response['SequenceNumber'])


def delete_1_message(queue):
    for message in queue.receive_messages(MessageAttributeNames=['All']):
        print('getting the oldest message in the queue')
    message.delete()
    print('oldest message delected...')

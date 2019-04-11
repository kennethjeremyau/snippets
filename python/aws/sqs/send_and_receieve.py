#!/usr/bin/env python

import boto3
import json

sqs = boto3.resource('sqs')
source = sqs.get_queue_by_name(QueueName='QUEUE')
sink = sqs.get_queue_by_name(QueueName='QUEUE')

while True:
    for msg in source.receive_messages():
        try:
            payload = json.loads(msg.body)
        except Exception as e:
            print ('ERROR {}'.format(e))
            continue

        try:
            sink.send_message(MessageBody=json.dumps(payload))
        except Exception as e:
            print ('ERROR {}'.format(e))

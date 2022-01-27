#!/usr/bin/env python

import boto3

sqs = boto3.resource('sqs', region_name='us-east-1')
q = sqs.get_queue_by_name(QueueName='QUEUE_NAME')

while True:
    for msg in q.receive_messages():
        try:
            payload = msg.body
            print(payload)
            q.delete_messages(Entries=[{
                'Id': msg.message_id,
                'ReceiptHandle': msg.receipt_handle
            }])
        except Exception as e:
            print ('ERROR {}'.format(e))
            continue

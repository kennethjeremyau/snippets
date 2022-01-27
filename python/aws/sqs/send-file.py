#!/usr/bin/env python3

import boto3
import sys

sqs = boto3.resource('sqs', region_name='us-east-1')
q = sqs.get_queue_by_name(QueueName='QUEUE_NAME')

for line in sys.stdin:
    msg = line.rstrip()
    print(msg)
    q.send_message(MessageBody=msg)

#!/usr/bin/env python

from boto import sqs
import time


connection = sqs.connect_to_region('us-east-1')
queue = connection.get_queue('queuename')
send_message(queue, '{{"key":"value"}}')

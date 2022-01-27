#!/usr/bin/env python

import boto3

session = boto3.Session()
credentials = session.get_credentials()
current_credentials = credentials.get_frozen_credentials()
print(current_credentials.access_key)
print(current_credentials.secret_key)

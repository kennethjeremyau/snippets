#!/usr/bin/env python

import psycopg2

connection = psycopg2.connect("""
    dbname='redshift_db'
    port='5439'
    user='username'
    password='password'
    host='host.us-east-1.redshift.amazonaws.com'
""")

query = """
COPY destination
FROM 's3://source'
CREDENTIALS 'aws_access_key_id={};aws_secret_access_key={}'
""".format(
    'AWS_ACCESS_KEY',
    'AWS_SECRET_KEY'
)

try:
    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
finally:
    cursor.close()
    connection.close()

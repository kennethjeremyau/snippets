import boto3

s3 = boto3.resource('s3')
obj = s3.Object('bucket', 'key')

for line in obj.get()['Body'].iter_lines():
    print(line)

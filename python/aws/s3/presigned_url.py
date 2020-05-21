import boto3
import requests

url = boto3.client('s3').generate_presigned_url(
    'put_object',
    dict(Bucket='BUCKET', Key='KEY'),
)

print(url)

with open('file.txt', 'rb') as f:
    r = requests.put(url, data=f)
    r.raise_for_status()

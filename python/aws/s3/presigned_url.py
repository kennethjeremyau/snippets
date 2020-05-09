import boto3

url = boto3.client('s3').generate_presigned_url(
        'put_object',
        dict(Bucket='bucket', Key='key'),
    )

print(url)

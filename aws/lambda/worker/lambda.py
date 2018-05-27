import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1')

user_data = """
#!/bin/bash

trap 'shutdown -h now' EXIT INT TERM

export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=
export AWS_DEFAULT_REGION=

# TODO
"""

def lambda_handler(event, context):
    instance = ec2.create_instances(
        ImageId = 'ami-2f39bf4b',
        MinCount = 1,
        MaxCount = 1,
        UserData = user_data,
        InstanceType = 'm5.large',
        BlockDeviceMappings=[{
            'DeviceName': '/dev/xvda',
            'Ebs': {
                'VolumeSize': 200
            }
        }],
        KeyName='worker',
        InstanceInitiatedShutdownBehavior = 'terminate',
        TagSpecifications = [{
            'ResourceType': 'instance',
            'Tags': [{
                'Key': 'Name',
                'Value': 'worker',
            }],
        }]
    )
    return 'ok'

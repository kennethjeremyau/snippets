import boto3
from botocore.credentials import RefreshableCredentials
from botocore.session import get_session

class RefreshableSessionHelper():

    def __init__(self, session_name, role_arn, region='us-east-1'):
        self.role_arn = role_arn
        self.session_name = session_name
        self.region = region
        self.sts_client = boto3.client('sts')

        credentials = self._refresh()
        session_credentials = RefreshableCredentials.create_from_metadata(
            metadata=credentials,
            refresh_using=self._refresh,
            method="sts-assume-role"
        )
        session = get_session()
        session._credentials = session_credentials
        session.set_config_variable("region", region)
        self.session = boto3.Session(botocore_session=session)

    def get_client(self, service):
        return self.session.client(service)

    def get_resource(self, service):
        return self.session.resource(service)

    def get_session(self):
        return self.session

    def _refresh(self):
        params = {
            "RoleArn": self.role_arn,
            "RoleSessionName": self.session_name,
            "DurationSeconds": 3600,
        }
        response = self.sts_client.assume_role(**params).get("Credentials")
        credentials = {
            "access_key": response.get("AccessKeyId"),
            "secret_key": response.get("SecretAccessKey"),
            "token": response.get("SessionToken"),
            "expiry_time": response.get("Expiration").isoformat(),
        }
        return credentials

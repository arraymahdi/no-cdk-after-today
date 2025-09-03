import boto3
from app.config.settings import settings

def get_boto3_session(region: str | None = None):
    return boto3.Session(
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        aws_session_token=settings.AWS_SESSION_TOKEN,
        region_name=region or settings.AWS_REGION
    )

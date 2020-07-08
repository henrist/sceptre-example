import boto3
from datetime import datetime
import json
import os

s3 = boto3.client("s3")

def handler(event, context):
    s3.put_object(
        Bucket=os.environ["BUCKET_NAME"],
        Key=datetime.utcnow().strftime("year=%Y/month=%m/day=%d/%H%M%S.json"),
        Body=json.dumps(event).encode("utf-8"),
    )

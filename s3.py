from imports import *
import boto3
from botocore.exceptions import ClientError

AWS_ACCESS_KEY_ID='AKIAZQL7LTOI3YH3OZ47'
AWS_SECRET_ACCESS_KEY='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'
Buckets='staging-hcms-textract'
folder_name="data/files/skills-observatory"
region="eu-west-2"

# Generate a random number between 1 and 10

agent_path="s3://staging-hcms-textract/data/files/hcms_skills/.csv"




s3_client = boto3.client(
        service_name='s3',
        region_name=region,
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY
    )

#response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)


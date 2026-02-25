import boto3
import os
from dotenv import load_dotenv

#load env variables
load_dotenv()

client = boto3.client('s3')
ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
BUCKET_NAME = os.getenv("TEST_BUCKET_NAME")

response = client.get_bucket_encryption(
    Bucket=BUCKET_NAME, # bucket name
    ExpectedBucketOwner= ACCOUNT_ID
)

print(response) # raw output
print(response['ServerSideEncryptionConfiguration'])
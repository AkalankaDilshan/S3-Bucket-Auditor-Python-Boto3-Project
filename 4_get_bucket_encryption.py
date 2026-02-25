import boto3
import os

client = boto3.client('s3')
ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")

response = client.get_bucket_encryption(
    Bucket='codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811', # bucket name
    ExpectedBucketOwner= ACCOUNT_ID
)

print(response) # raw output
print(response['ServerSideEncryptionConfiguration'])
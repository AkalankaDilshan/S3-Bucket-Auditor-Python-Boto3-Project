import boto3
import os

client = boto3.client('s3')
ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")

response = client.get_bucket_versioning(
    Bucket='akalanka-test-bucket4f45',
    ExpectedBucketOwner=ACCOUNT_ID #account id
)

print(response) # full one

status = response.get('Status', 'Disabled')
### The Anatomy of .get()
#In Python, you can access dictionary values in two ways:
#Square Brackets: response['Status'] — Risky.
#The .get() Method: response.get('Status', 'Disabled') — Safe.

#The syntax follows this logic: dictionary.get(key, default_value)

print(status) # here we clearly see versioning enable or not


    
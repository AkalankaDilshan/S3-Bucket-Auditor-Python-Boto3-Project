import boto3
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv() ## this is compulsory 

client = boto3.client('s3')
ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
BUCKET_NAME= os.getenv("TEST_BUCKET_NAME")

response = client.get_bucket_versioning(
    Bucket=BUCKET_NAME,
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


    
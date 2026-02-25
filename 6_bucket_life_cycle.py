import boto3 
import logging
from botocore.exceptions import ClientError
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

client = boto3.client('s3')
ACCOUNT_ID = os.getenv("AWS_ACCOUNT_ID")
BUCKET_NAME = os.getenv('TEST_BUCKET_NAME')

# Check if required environment variables are set
if not BUCKET_NAME:
    print("Error: TEST_BUCKET_NAME environment variable is not set")
    print("Please check your .env file or set the environment variable")
    exit(1)

try: 
    # Build kwargs conditionally — only include ExpectedBucketOwner if ACCOUNT_ID is set
    lifecycle_kwargs = {'Bucket': BUCKET_NAME}
    if ACCOUNT_ID:
        lifecycle_kwargs['ExpectedBucketOwner'] = ACCOUNT_ID

    response = client.get_bucket_lifecycle(**lifecycle_kwargs)
    #**kwargs stands for "Keyword Arguments". 
    # It's a Python feature that allows you to pass a variable number of keyword arguments to a function.

    #print(response) # get all data
    lifecycle_status = response.get ('Rules')
    lifecycle_transition = response['Rules'][0]['Transition'] # .get not working for this one because return has complex data type
    
    
    
    print(f'Lifecycle Rules: {lifecycle_status}')
    print(f'Lifecycle Transition: {lifecycle_transition}') # Lifecycle Transition: {'Days': 30, 'StorageClass': 'DEEP_ARCHIVE'}
    
except ClientError as e:
    #logging.error(e)
    print('No Such Lifecycle Configuration')
    

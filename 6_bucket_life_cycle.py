import boto3 
import logging
from botocore.exceptions import ClientError
import os

client = boto3.client('s3')
ACCOUNT_ID = os.environ.get("AWS_ACCOUNT_ID")

try: 
    response = client.get_bucket_lifecycle(
        Bucket='akalanka-test-bucket4f45',
        ExpectedBucketOwner=ACCOUNT_ID
    )

    #print(response) # get all data
    lifecycle_status = response.get ('Rules')
    lifecycle_transition = response['Rules'][0]['Transition'] # .get not working for this one because return has complex data type
    
    
    
    print(f'Lifecycle Rules: {lifecycle_status}')
    print(f'Lifecycle Transition: {lifecycle_transition}') # Lifecycle Transition: {'Days': 30, 'StorageClass': 'DEEP_ARCHIVE'}
    
except ClientError as e:
    #logging.error(e)
    print('No Such Lifecycle Configuration')
    

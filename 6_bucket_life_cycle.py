import boto3 
import logging
from botocore.exceptions import ClientError

client = boto3.client('s3')

try: 
    response = client.get_bucket_lifecycle(
        Bucket='akalanka-test-bucket4f45',
        ExpectedBucketOwner='375353319115'
    )

    #print(response) # get all data
    lifecycle_status = response.get ('Rules')
    lifecycle_transition = response['Rules'][0]['Transition'] # .get not working for this one because return has complex data type
    
    
    
    print(f'Lifecycle Rules: {lifecycle_status}')
    print(f'Lifecycle Transition: {lifecycle_transition}') # Lifecycle Transition: {'Days': 30, 'StorageClass': 'DEEP_ARCHIVE'}
    
except ClientError as e:
    #logging.error(e)
    print('No Such Lifecycle Configuration')
    

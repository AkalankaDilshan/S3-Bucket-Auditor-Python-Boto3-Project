import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()

    
'''Create Bucket'''
def create_s3_bucket (bucket_name, region ='us-east-1'):
    try: 
        bucket_config = {}
        s3_client = boto3.client('s3', region_name = region)
        
        if region != 'us-east-1':
            bucket_config['CreateBucketConfiguration'] = {'LocationConstraint': region}
            
        # create bucket
        s3_client.create_bucket(Bucket=bucket_name, **bucket_config)
        #The ** operator takes a dictionary and 
        #unpacks it into keyword arguments. It's like telling 
        #Python: "Take this dictionary and pass
        #its contents as separate named arguments to the function
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Call function
#create_s3_bucket("akalanka-test-bucket4f45")

    

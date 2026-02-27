import boto3
import logging
from botocore.exceptions import ClientError

#client = boto3.client('s3')


class S3report:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.client = boto3.client('s3')
        
    # bucket encryption method
    def bucket_encryption(self) -> bool:
        try:
            encryption_rule = self.client.get_bucket_encryption(Bucket = self.bucket_name)
            print(f'Bucket encryption rule:{encryption_rule['ServerSideEncryptionConfiguration']}')
        except ClientError as e :
            if e.response["Error"]["Code"] == "ServerSideEncryptionConfigurationNotFoundError":
                print("WARNING: No encryption configured!")
            else:
                print(f"Error checking encryption for {self.bucket_name}: {e}")
                return False
            return True
    
    # bucket life cycle module
    def bucket_lifecycle_configuration(self) -> bool:
        try:
            #response = client.get_bucket_lifecycle(Bucket=bucket_name) #Deprecated API: get_bucket_lifecycle so use new one
            response = self.client.get_bucket_lifecycle_configuration(Bucket=self.bucket_name)
            lifecycle_status = response.get ('Rules')
            print(f'Lifecycle Rules: {lifecycle_status}')
        
        except ClientError as e:
            #logging.error(e) ## if want to see log uncomment this one 
            print('No Such Lifecycle Configuration')
            return False
        return True
            
## get all s3 bucket name and store it on list
## create list
name_list = []
bucket_name_list = client.list_buckets()
for i in bucket_name_list['Buckets']:
    #print(f'{i['Name']}\n\n')
    name_list.append(i['Name'])


# bucket life cycle function
def bucket_lifecycle_configuration(bucket_name):
    try:
        #response = client.get_bucket_lifecycle(Bucket=bucket_name) #Deprecated API: get_bucket_lifecycle so use new one
        response = client.get_bucket_lifecycle_configuration(Bucket=bucket_name)
        lifecycle_status = response.get ('Rules')
        print(f'Lifecycle Rules: {lifecycle_status}')
        
    except ClientError as e:
        #logging.error(e) ## if want to see log uncomment this one 
        print('No Such Lifecycle Configuration')
        return False
    
    return True
     
     
# bucket versioning function
def bucket_versioning(bucket_name: str) -> bool:
    try:
        versioning_response = client.get_bucket_versioning(
        Bucket = bucket_name
        )
        versioning_status = versioning_response.get('Status', 'Disabled')
        print(f'Bucket verioning {versioning_status}') 
        
    except ClientError as e:
        print(f'Error checking bucket versioning for {bucket_name}: {e}')
        return False
    return True     
      
## bucket public access rule checker function
def bucket_public_access_checker(bucket_name: str) -> bool:
    try:
        policy = client.get_public_access_block(
        Bucket = bucket_name
        )
        for key, value in policy['PublicAccessBlockConfiguration'].items():
            print(f'{key} : {value}')
        
    except ClientError as e:
        print(f"Error checking public access for {bucket_name}: {e}")
        return False
    return True
        
# main function
def main():
    for b_name in name_list:
        print(f'\n\nBucket name: {b_name}')
    
        # bucket encryption
        bucket_encryption(b_name)
    
        # bucket versioning
        #bucket_versioning(b_name)
    
        # Bucket lifecycle 
        #bucket_lifecycle_configuration(b_name)
    
        # bucket public access or not
        #bucket_public_access_checker(b_name)
    
# With the guard    
if __name__ == "__main__":
    main()
        





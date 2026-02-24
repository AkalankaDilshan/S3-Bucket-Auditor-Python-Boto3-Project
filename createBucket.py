import logging
import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
response = s3.list_buckets()

#print(response) # this give nested Dictionary, key: value pair

#print(response['Buckets']) # that Dictionary has buckets list
#print(f" first bucket details: {response['Buckets'][0]}") # here get first item in buckets list, but first item is another dictionary
#print(f"first bucket name: {response['Buckets'][0]["Name"]}")

# List all the existing buckets
for i in response['Buckets'] :
    print(f"{i["Name"]}")
    
'''Create Bucket'''
def 
    

import boto3
import json

client = boto3.client('s3')

# list_bucket = client.list_buckets()

# for i in list_bucket['Buckets']:
#     print(f'{i["Name"]} \n')


response = client.get_bucket_policy(
    Bucket= "codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811",
)
# output The bucket policy as a JSON document.
#print(response['Policy']) # mekan output ek enwa but set na.

policy = json.loads(response['Policy'])
print(f'{policy}\n\n\n')

# get_bucket_policy_status, public or not

bucket_status = client.get_bucket_policy_status(
    Bucket= "codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811",
)

print(bucket_status,"\n") # get full policy status
print(f'{bucket_status['PolicyStatus']}\n') # get public access policy statment
print(f'{bucket_status['PolicyStatus']['IsPublic']}\n') ## get full clear answer
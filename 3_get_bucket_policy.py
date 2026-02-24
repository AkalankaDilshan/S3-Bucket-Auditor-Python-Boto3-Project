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

# get_bucket_policy_status

bucket_policy_status = client.get_bucket_policy_status(
    Bucket= "codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811",
)

print(bucket_policy_status,"\n") # get full policy status
print(f'{bucket_policy_status['PolicyStatus']}\n') # get public access policy statment
print(f'{bucket_policy_status['PolicyStatus']['IsPublic']}\n') ## get full clear answer
## i feel above one not necessary

# Retrieves the PublicAccessBlock configuration for S3
s3_public_access_policy = client.get_public_access_block(
    Bucket='codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811',
    ExpectedBucketOwner='375353319115' #account id
)

print(s3_public_access_policy,"\n\n\n") # all thing with meta data
print(f'{s3_public_access_policy['PublicAccessBlockConfiguration']}\n\n')

## good method
for key, value in s3_public_access_policy['PublicAccessBlockConfiguration'].items():
    print(f'{key} : {value}\n') # .items is dictionary method, it seperate each item to tuples.
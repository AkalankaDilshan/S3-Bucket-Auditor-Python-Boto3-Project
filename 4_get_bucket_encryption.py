import boto3

client = boto3.client('s3')

response = client.get_bucket_encryption(
    Bucket='codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811', # bucket name
    ExpectedBucketOwner='375353319115' #account id
)

print(response) # raw output
print(response['ServerSideEncryptionConfiguration'])
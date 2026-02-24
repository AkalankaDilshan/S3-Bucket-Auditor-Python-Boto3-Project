import boto3

client = boto3.client('s3')

response = client.get_bucket_versioning(
    Bucket='codepipeline-eu-north-1-3350963aa07b-4ea1-9a94-926cfb3be811',
    ExpectedBucketOwner='375353319115' #account id
)

print(response) # full one

status = response.get('Status')
print(status) # here we clearly see versioning enable or not

if status == 'Enabled':
    print(status)
else:
    print("Versioning is NOT ENABLED")
    
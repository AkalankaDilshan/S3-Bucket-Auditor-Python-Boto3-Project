import boto3

client = boto3.client('s3')

## get all s3 bucket name and store it on stack
## create list
name_list = []

bucket_name_list = client.list_buckets()

for i in bucket_name_list['Buckets']:
    #print(f'{i['Name']}\n\n')
    name_list.append(i['Name'])

# bucket public access or not
for j in name_list:
    policy = client.get_public_access_block(
        Bucket = j
    )
    
    #encryption
    encryption_rule = client.get_bucket_encryption(
        Bucket = j
    )
    print(f'\n\nBucket name: {j}')
    print(encryption_rule['ServerSideEncryptionConfiguration'])
    # bucket public access or not
    for key, value in policy['PublicAccessBlockConfiguration'].items():
        print(f'{key} : {value}')
        
        
    
  


# missing encryption



# bucket versioning

# bucket life cycle 


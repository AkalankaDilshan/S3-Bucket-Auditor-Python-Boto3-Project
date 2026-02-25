import boto3

client = boto3.client('s3')

## get all s3 bucket name and store it on list
## create list
name_list = []

bucket_name_list = client.list_buckets()

for i in bucket_name_list['Buckets']:
    #print(f'{i['Name']}\n\n')
    name_list.append(i['Name'])

# bucket public access or not
for j in name_list:
    print(f'\n\nBucket name: {j}')
    # missing encryption
    encryption_rule = client.get_bucket_encryption(
        Bucket = j
    )
    print(encryption_rule['ServerSideEncryptionConfiguration'])
    
    # bucket versioning
    versioning_response = client.get_bucket_versioning(
        Bucket = j
    )
    
    versioning_status = versioning_response.get('Status', 'Disabled')
    print(f'Bucket verioning {versioning_status}') 
    
    # bucket public access or not
    policy = client.get_public_access_block(
        Bucket = j
    )
    for key, value in policy['PublicAccessBlockConfiguration'].items():
        print(f'{key} : {value}')
        


# bucket life cycle 


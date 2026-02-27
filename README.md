# S3 Bucket Auditor

A simple Python script that checks all your AWS S3 buckets and tells you if any of them have security issues.

## What it does

It scans every S3 bucket in your AWS account and checks four things:

- **Encryption** — Is the bucket encrypted?
- **Versioning** — Is versioning turned on?
- **Lifecycle Rules** — Are there any lifecycle rules set up?
- **Public Access** — Is the bucket blocking public access?

It then prints a report in your terminal for each bucket.

## Requirements

- Python 3
- AWS credentials configured on your machine (`aws configure`)
- The `boto3` library installed

```bash
pip install boto3
```

## How to run

```bash
python main.py
```

That's it. The script will automatically find all your buckets and check each one.

## AWS Permissions needed

Your AWS user or role needs these permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:ListAllMyBuckets",
        "s3:GetBucketEncryption",
        "s3:GetBucketVersioning",
        "s3:GetBucketLifecycleConfiguration",
        "s3:GetBucketPublicAccessBlock"
      ],
      "Resource": "*"
    }
  ]
}
```
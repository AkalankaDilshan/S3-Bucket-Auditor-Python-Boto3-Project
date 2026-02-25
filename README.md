# S3-Bucket-Auditor-Python-Boto3-Project

scan all buckets for public access, missing encryption, and no versioning. Output a report.


**Recommendation:** Minimum IAM policy:

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
        "s3:GetBucketPublicAccessBlock",
        "s3:GetBucketPolicy",
        "s3:GetBucketPolicyStatus"
      ],
      "Resource": "*"
    }
  ]
}
```
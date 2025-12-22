# IAM Security

## Overview

Identity and access management for ML workloads.

## SageMaker Execution Roles

Role that SageMaker assumes to access AWS resources.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "sagemaker.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Common Permissions

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:GetObject", "s3:PutObject", "s3:ListBucket"],
      "Resource": ["arn:aws:s3:::my-bucket", "arn:aws:s3:::my-bucket/*"]
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:*:*:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ecr:GetAuthorizationToken",
        "ecr:BatchGetImage",
        "ecr:GetDownloadUrlForLayer"
      ],
      "Resource": "*"
    }
  ]
}
```

## AWS KMS

Encryption at rest for ML data and models.

### Creating a KMS Key

```python
import boto3

kms = boto3.client("kms")

response = kms.create_key(
    Description="Key for ML workloads",
    KeyUsage="ENCRYPT_DECRYPT",
    Tags=[{"TagKey": "Project", "TagValue": "ML"}]
)

key_id = response["KeyMetadata"]["KeyId"]
```

### Using KMS with SageMaker

```python
from sagemaker.estimator import Estimator

estimator = Estimator(
    ...
    output_kms_key=kms_key_arn,
    volume_kms_key=kms_key_arn
)
```

## AWS Secrets Manager

Store sensitive credentials securely.

```python
import boto3
import json

secrets_client = boto3.client("secretsmanager")

# Create secret
secrets_client.create_secret(
    Name="ml/database-credentials",
    SecretString=json.dumps({
        "username": "admin",
        "password": "secret123"
    })
)

# Retrieve secret
response = secrets_client.get_secret_value(SecretId="ml/database-credentials")
credentials = json.loads(response["SecretString"])
```

## VPC Configuration

Isolate SageMaker resources in VPC.

```python
from sagemaker import Estimator

estimator = Estimator(
    ...
    subnets=["subnet-abc123", "subnet-def456"],
    security_group_ids=["sg-12345678"]
)
```

### VPC Endpoints

| Endpoint          | Purpose                    |
| ----------------- | -------------------------- |
| sagemaker.api     | SageMaker API calls        |
| sagemaker.runtime | Inference calls            |
| s3                | S3 access without internet |

## Best Practices

!!! tip "Security Best Practices" 1. Use least privilege IAM policies 2. Enable encryption at rest with KMS 3. Use VPC for network isolation 4. Store secrets in Secrets Manager 5. Enable CloudTrail for auditing 6. Use S3 bucket policies for data access control

## Exam Tips

!!! warning "Key Points" - Execution role is assumed by SageMaker - KMS for encryption at rest - Secrets Manager for credentials - VPC for network isolation - VPC endpoints for private access

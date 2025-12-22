# AWS Services Reference

Quick reference for AWS services covered in the MLA-C01 exam.

## Core ML Services

| Service                                             | Description          | Key Use Cases               |
| --------------------------------------------------- | -------------------- | --------------------------- |
| [SageMaker](sagemaker.md)                           | Full ML platform     | Training, deployment, MLOps |
| [Bedrock](bedrock.md)                               | Foundation models    | GenAI, fine-tuning          |
| [Glue](glue.md)                                     | ETL and data catalog | Data preparation            |
| [Comprehend/Rekognition](comprehend-rekognition.md) | AI services          | NLP, computer vision        |
| [Other ML Services](other-ml-services.md)           | Specialized AI       | Lex, Polly, Personalize     |

## Service Categories

### Data Preparation

- Amazon S3 - Object storage
- AWS Glue - ETL, data catalog
- Amazon Kinesis - Streaming data
- AWS Lake Formation - Data lake management
- Amazon Athena - Query service

### Model Development

- Amazon SageMaker - Training, tuning
- Amazon Bedrock - Foundation models
- SageMaker JumpStart - Pre-trained models

### Deployment

- SageMaker Endpoints - Inference
- Amazon ECR - Container registry
- AWS Lambda - Serverless compute

### Orchestration

- SageMaker Pipelines - ML workflows
- AWS Step Functions - Orchestration
- Amazon MWAA - Apache Airflow

### Monitoring

- Amazon CloudWatch - Metrics, logs
- AWS CloudTrail - Audit logging
- SageMaker Model Monitor - Drift detection

### Security

- AWS IAM - Access management
- AWS KMS - Encryption
- AWS Secrets Manager - Secrets
- Amazon Macie - Data protection

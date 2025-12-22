# Compliance

## Overview

Ensuring ML solutions meet compliance and governance requirements.

## Amazon Macie

Discover and protect sensitive data in S3.

### Key Features

- Automatic sensitive data discovery
- PII detection
- Custom data identifiers
- Findings and alerts

```python
import boto3

macie = boto3.client("macie2")

# Enable Macie
macie.enable_macie()

# Create classification job
macie.create_classification_job(
    name="ml-data-scan",
    s3JobDefinition={
        "bucketDefinitions": [{
            "accountId": "123456789012",
            "buckets": ["my-ml-bucket"]
        }]
    },
    jobType="ONE_TIME"
)
```

## AWS Config

Track resource compliance.

### SageMaker Config Rules

| Rule                                                | Description        |
| --------------------------------------------------- | ------------------ |
| sagemaker-endpoint-configuration-kms-key-configured | Endpoint uses KMS  |
| sagemaker-notebook-instance-inside-vpc              | Notebook in VPC    |
| sagemaker-notebook-no-direct-internet-access        | No direct internet |

### Custom Config Rule

```python
# Lambda function for custom rule
def evaluate_compliance(configuration_item):
    if configuration_item["resourceType"] != "AWS::SageMaker::Endpoint":
        return "NOT_APPLICABLE"

    # Check endpoint configuration
    config = configuration_item["configuration"]
    if config.get("kmsKeyId"):
        return "COMPLIANT"
    return "NON_COMPLIANT"
```

## Data Governance

### AWS Lake Formation

Fine-grained access control for data lakes.

- Row-level security
- Column-level security
- Data sharing across accounts

### SageMaker Governance

| Feature          | Purpose                    |
| ---------------- | -------------------------- |
| Model Cards      | Document model details     |
| Model Registry   | Version and approve models |
| Lineage Tracking | Track data to model        |

## Model Cards

Document model information for governance.

```python
from sagemaker.model_card import ModelCard, ModelOverview

model_card = ModelCard(
    name="customer-churn-model",
    status="Draft",
    model_overview=ModelOverview(
        model_description="Predicts customer churn probability",
        model_creator="Data Science Team",
        problem_type="Binary Classification"
    ),
    intended_uses=IntendedUses(
        purpose_of_model="Identify at-risk customers",
        intended_uses="Customer retention campaigns",
        factors_affecting_model_efficiency="Data recency",
        risk_rating="Medium"
    )
)

model_card.create()
```

## Audit Logging

### CloudTrail for Compliance

```sql
-- Find all model deployments
SELECT eventTime, userIdentity.userName, requestParameters.endpointName
FROM cloudtrail_logs
WHERE eventName = 'CreateEndpoint'
  AND eventTime > '2024-01-01'
ORDER BY eventTime DESC
```

## Exam Tips

!!! warning "Key Points" - Macie for sensitive data discovery - Config rules for compliance checking - Lake Formation for data governance - Model Cards for model documentation - CloudTrail for audit logging

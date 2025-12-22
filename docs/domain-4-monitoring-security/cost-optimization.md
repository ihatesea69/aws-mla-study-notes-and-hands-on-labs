# Cost Optimization

## Overview

Strategies for optimizing ML costs on AWS.

## AWS Cost Management Tools

| Tool              | Purpose                       |
| ----------------- | ----------------------------- |
| Cost Explorer     | Visualize and analyze costs   |
| AWS Budgets       | Set cost alerts               |
| Savings Plans     | Commit to usage for discounts |
| Spot Instances    | Use spare capacity            |
| Compute Optimizer | Right-sizing recommendations  |

## SageMaker Cost Optimization

### Training Costs

**Spot Training**

Save up to 90% on training costs.

```python
estimator = Estimator(
    ...
    use_spot_instances=True,
    max_wait=3600,
    max_run=1800,
    checkpoint_s3_uri="s3://bucket/checkpoints/"
)
```

**Right-sizing Instances**

| Instance Type     | Use Case         |
| ----------------- | ---------------- |
| ml.m5.\*          | General purpose  |
| ml.c5.\*          | CPU-intensive    |
| ml.p3._/ml.g4dn._ | Deep learning    |
| ml.r5.\*          | Memory-intensive |

**Managed Warm Pools**

Reduce training startup time.

```python
estimator = Estimator(
    ...
    keep_alive_period_in_seconds=3600  # 1 hour
)
```

### Inference Costs

**Serverless Endpoints**

Pay per request, no idle costs.

```python
serverless_config = ServerlessInferenceConfig(
    memory_size_in_mb=2048,
    max_concurrency=10
)
```

**Multi-Model Endpoints**

Host multiple models on single instance.

```python
mme = MultiDataModel(
    name="mme-endpoint",
    model_data_prefix="s3://bucket/models/",
    image_uri=image_uri,
    role=role
)
```

**Auto Scaling**

Scale to zero during low traffic (Serverless) or minimum capacity.

### Storage Costs

- Use S3 lifecycle policies for old data
- Clean up unused model artifacts
- Use appropriate storage classes

## AWS Budgets

```python
import boto3

budgets = boto3.client("budgets")

budgets.create_budget(
    AccountId="123456789012",
    Budget={
        "BudgetName": "ML-Monthly-Budget",
        "BudgetLimit": {"Amount": "1000", "Unit": "USD"},
        "TimeUnit": "MONTHLY",
        "BudgetType": "COST"
    },
    NotificationsWithSubscribers=[{
        "Notification": {
            "NotificationType": "ACTUAL",
            "ComparisonOperator": "GREATER_THAN",
            "Threshold": 80,
            "ThresholdType": "PERCENTAGE"
        },
        "Subscribers": [{
            "SubscriptionType": "EMAIL",
            "Address": "team@example.com"
        }]
    }]
)
```

## Cost Allocation Tags

Track costs by project, team, or environment.

```python
sagemaker.create_training_job(
    ...
    Tags=[
        {"Key": "Project", "Value": "CustomerChurn"},
        {"Key": "Environment", "Value": "Production"},
        {"Key": "Team", "Value": "DataScience"}
    ]
)
```

## Exam Tips

!!! warning "Key Strategies" - Spot Instances for training (up to 90% savings) - Serverless endpoints for variable traffic - Multi-model endpoints for many models - Right-size instances with Compute Optimizer - Use Budgets for cost alerts

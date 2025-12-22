# Model Versioning

## Overview

Managing model versions with SageMaker Model Registry.

## Model Registry

Centralized repository for model versioning.

### Key Concepts

| Concept             | Description                  |
| ------------------- | ---------------------------- |
| Model Package Group | Collection of model versions |
| Model Package       | Single model version         |
| Approval Status     | Pending, Approved, Rejected  |
| Model Metrics       | Performance metrics          |

### Creating a Model Package Group

```python
import boto3

sm_client = boto3.client("sagemaker")

sm_client.create_model_package_group(
    ModelPackageGroupName="my-model-group",
    ModelPackageGroupDescription="Production models for customer churn"
)
```

### Registering a Model

```python
from sagemaker.model import Model

model = Model(
    image_uri=inference_image,
    model_data="s3://bucket/model.tar.gz",
    role=role
)

model_package = model.register(
    model_package_group_name="my-model-group",
    content_types=["application/json"],
    response_types=["application/json"],
    inference_instances=["ml.m5.large"],
    transform_instances=["ml.m5.large"],
    approval_status="PendingManualApproval",
    model_metrics={
        "ModelQuality": {
            "Statistics": {
                "ContentType": "application/json",
                "S3Uri": "s3://bucket/metrics.json"
            }
        }
    }
)
```

### Approval Workflow

```python
# Approve a model
sm_client.update_model_package(
    ModelPackageArn=model_package_arn,
    ModelApprovalStatus="Approved"
)

# Reject a model
sm_client.update_model_package(
    ModelPackageArn=model_package_arn,
    ModelApprovalStatus="Rejected"
)
```

## Model Lineage

Track the complete lifecycle of a model.

```python
from sagemaker.lineage.context import Context
from sagemaker.lineage.artifact import Artifact

# Query lineage
artifacts = Artifact.list(source_uri="s3://bucket/model.tar.gz")
```

## SageMaker Experiments

Track experiments and compare results.

```python
from sagemaker.experiments import Run

with Run(experiment_name="my-experiment", run_name="run-1") as run:
    run.log_parameter("learning_rate", 0.01)
    run.log_metric("accuracy", 0.95)
    run.log_artifact(name="model", value="s3://bucket/model.tar.gz")
```

## Best Practices

!!! tip "Versioning Best Practices" 1. Use Model Registry for all production models 2. Implement approval workflows for governance 3. Track metrics with each model version 4. Use lineage for reproducibility 5. Tag models with relevant metadata

## Exam Tips

!!! warning "Key Points" - Model Registry for versioning and governance - Approval status gates deployment - Lineage tracks data→training→model→deployment - Experiments for comparing model runs

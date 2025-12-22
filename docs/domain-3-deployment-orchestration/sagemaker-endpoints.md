# SageMaker Endpoints

## Overview

Deploy models for real-time inference.

## Endpoint Types

### Real-time Inference

Always-on endpoints for low-latency predictions.

```python
from sagemaker.model import Model

model = Model(
    image_uri=inference_image,
    model_data="s3://bucket/model.tar.gz",
    role=role
)

predictor = model.deploy(
    initial_instance_count=2,
    instance_type="ml.m5.large",
    endpoint_name="my-endpoint"
)

# Invoke
response = predictor.predict(data)
```

### Serverless Inference

Pay-per-request with automatic scaling.

```python
from sagemaker.serverless import ServerlessInferenceConfig

serverless_config = ServerlessInferenceConfig(
    memory_size_in_mb=2048,
    max_concurrency=10
)

predictor = model.deploy(
    serverless_inference_config=serverless_config,
    endpoint_name="serverless-endpoint"
)
```

### Asynchronous Inference

For large payloads and long processing times.

```python
from sagemaker.async_inference import AsyncInferenceConfig

async_config = AsyncInferenceConfig(
    output_path="s3://bucket/async-output/",
    max_concurrent_invocations_per_instance=4,
    notification_config={
        "SuccessTopic": success_topic_arn,
        "ErrorTopic": error_topic_arn
    }
)

predictor = model.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1,
    async_inference_config=async_config
)
```

## Multi-Model Endpoints

Host multiple models on single endpoint.

```python
from sagemaker.multidatamodel import MultiDataModel

mme = MultiDataModel(
    name="multi-model-endpoint",
    model_data_prefix="s3://bucket/models/",
    image_uri=inference_image,
    role=role
)

predictor = mme.deploy(
    initial_instance_count=1,
    instance_type="ml.m5.large"
)

# Invoke specific model
predictor.predict(data, target_model="model-a.tar.gz")
```

## Inference Components

Share resources across models.

- Copy-based scaling
- Fine-grained resource allocation
- Cost optimization for multiple models

## Endpoint Comparison

| Feature     | Real-time   | Serverless  | Async       |
| ----------- | ----------- | ----------- | ----------- |
| Cold Start  | No          | Yes         | No          |
| Max Payload | 6 MB        | 6 MB        | 1 GB        |
| Max Timeout | 60s         | 60s         | 15 min      |
| Scaling     | Manual/Auto | Automatic   | Manual/Auto |
| Billing     | Per hour    | Per request | Per hour    |

## Exam Tips

!!! warning "Endpoint Selection" - Real-time: Consistent traffic, low latency required - Serverless: Variable traffic, cost sensitive - Async: Large payloads, long processing - Multi-model: Many similar models, cost optimization

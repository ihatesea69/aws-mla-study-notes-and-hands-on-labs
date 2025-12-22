# Lab 04: Endpoint Deployment

**Domain**: 3 - Deployment & Orchestration  
**Difficulty**: Medium  
**Time**: 45 minutes

## Objective

Deploy models using different SageMaker endpoint types.

## Prerequisites

- Trained model in S3 (from Lab 02)
- SageMaker execution role

## Steps

### Step 1: Real-time Endpoint

```python
from sagemaker.model import Model

# Create model
model = Model(
    image_uri=xgb_image,
    model_data=model_artifact,
    role=role,
    sagemaker_session=sagemaker_session
)

# Deploy real-time endpoint
predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    endpoint_name='xgb-realtime-endpoint'
)

# Test prediction
import numpy as np
test_data = np.array([[0.5, 0.3, 0.2, 0.4, 0.1, 0.6, 0.7, 0.8]])
result = predictor.predict(test_data)
print(f"Prediction: {result}")
```

### Step 2: Serverless Endpoint

```python
from sagemaker.serverless import ServerlessInferenceConfig

serverless_config = ServerlessInferenceConfig(
    memory_size_in_mb=2048,
    max_concurrency=5
)

# Deploy serverless endpoint
serverless_predictor = model.deploy(
    serverless_inference_config=serverless_config,
    endpoint_name='xgb-serverless-endpoint'
)

# Test (note: may have cold start delay)
result = serverless_predictor.predict(test_data)
print(f"Serverless prediction: {result}")
```

### Step 3: Async Endpoint

```python
from sagemaker.async_inference import AsyncInferenceConfig

async_config = AsyncInferenceConfig(
    output_path=f's3://{bucket}/{prefix}/async-output/',
    max_concurrent_invocations_per_instance=4
)

# Deploy async endpoint
async_predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    async_inference_config=async_config,
    endpoint_name='xgb-async-endpoint'
)
```

### Step 4: Invoke Async Endpoint

```python
import json

# Upload input to S3
input_data = json.dumps(test_data.tolist())
input_key = f'{prefix}/async-input/input.json'
s3_client = boto3.client('s3')
s3_client.put_object(Bucket=bucket, Key=input_key, Body=input_data)

# Invoke async
sm_runtime = boto3.client('sagemaker-runtime')
response = sm_runtime.invoke_endpoint_async(
    EndpointName='xgb-async-endpoint',
    InputLocation=f's3://{bucket}/{input_key}',
    ContentType='application/json'
)

output_location = response['OutputLocation']
print(f"Output will be at: {output_location}")
```

### Step 5: Compare Endpoints

| Endpoint Type | Latency  | Cost              | Use Case         |
| ------------- | -------- | ----------------- | ---------------- |
| Real-time     | Low      | High (always-on)  | Interactive apps |
| Serverless    | Variable | Low (pay-per-use) | Variable traffic |
| Async         | High     | Medium            | Large payloads   |

## Verification

- All three endpoints deployed successfully
- Predictions returned correctly
- Understand trade-offs between endpoint types

## Cleanup

```python
# Delete all endpoints
for endpoint in ['xgb-realtime-endpoint', 'xgb-serverless-endpoint', 'xgb-async-endpoint']:
    try:
        sm_client.delete_endpoint(EndpointName=endpoint)
        sm_client.delete_endpoint_config(EndpointConfigName=endpoint)
    except:
        pass

# Delete model
sm_client.delete_model(ModelName=model.name)
```

## Key Takeaways

!!! note "Exam Points" - Real-time: Consistent, low-latency needs - Serverless: Cost optimization, variable traffic - Async: Large payloads, long processing - Always clean up endpoints to avoid charges

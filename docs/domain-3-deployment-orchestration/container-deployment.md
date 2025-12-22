# Container Deployment

## Overview

Deploying ML models using containers on AWS.

## Amazon ECR

Container registry for storing Docker images.

```bash
# Build and push image
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin account.dkr.ecr.us-east-1.amazonaws.com

docker build -t my-inference-image .
docker tag my-inference-image:latest account.dkr.ecr.us-east-1.amazonaws.com/my-repo:latest
docker push account.dkr.ecr.us-east-1.amazonaws.com/my-repo:latest
```

## SageMaker Container Requirements

### Directory Structure

```
/opt/ml/
├── model/           # Model artifacts
├── input/
│   ├── config/      # Hyperparameters, resource config
│   └── data/        # Training data channels
└── output/          # Model output, failure info
```

### Inference Container

```dockerfile
FROM python:3.9-slim

RUN pip install flask gunicorn scikit-learn

COPY inference.py /opt/program/
COPY serve /opt/program/

ENV PATH="/opt/program:${PATH}"

WORKDIR /opt/program

ENTRYPOINT ["python", "serve"]
```

### Required Endpoints

| Endpoint     | Method | Purpose            |
| ------------ | ------ | ------------------ |
| /ping        | GET    | Health check       |
| /invocations | POST   | Inference requests |

```python
# serve.py
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return "", 200

@app.route("/invocations", methods=["POST"])
def invocations():
    data = request.get_json()
    prediction = model.predict(data)
    return json.dumps({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

## Bring Your Own Container (BYOC)

```python
from sagemaker.model import Model

model = Model(
    image_uri="account.dkr.ecr.region.amazonaws.com/my-repo:latest",
    model_data="s3://bucket/model.tar.gz",
    role=role
)

model.deploy(
    instance_type="ml.m5.large",
    initial_instance_count=1
)
```

## ECS/EKS Deployment

For non-SageMaker deployments.

### ECS

```yaml
# task-definition.json
{
  "family": "ml-inference",
  "containerDefinitions":
    [
      {
        "name": "inference",
        "image": "account.dkr.ecr.region.amazonaws.com/my-repo:latest",
        "memory": 2048,
        "cpu": 1024,
        "portMappings": [{ "containerPort": 8080 }],
      },
    ],
}
```

### EKS

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-inference
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-inference
  template:
    spec:
      containers:
        - name: inference
          image: account.dkr.ecr.region.amazonaws.com/my-repo:latest
          ports:
            - containerPort: 8080
```

## Exam Tips

!!! warning "Key Points" - ECR for storing container images - SageMaker containers need /ping and /invocations - BYOC for custom frameworks - ECS/EKS for non-SageMaker deployments

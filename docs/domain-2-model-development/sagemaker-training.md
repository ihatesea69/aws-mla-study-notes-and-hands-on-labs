# SageMaker Training

## Overview

Amazon SageMaker provides managed infrastructure for training ML models.

## Training Job Components

```python
from sagemaker.estimator import Estimator

estimator = Estimator(
    image_uri=training_image,
    role=role,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    output_path="s3://bucket/output/",
    hyperparameters={
        "epochs": 10,
        "learning_rate": 0.01
    }
)

estimator.fit({
    "train": "s3://bucket/train/",
    "validation": "s3://bucket/validation/"
})
```

## Instance Types

| Category          | Instance Types     | Use Case         |
| ----------------- | ------------------ | ---------------- |
| General Purpose   | ml.m5.\*           | Balanced compute |
| Compute Optimized | ml.c5.\*           | CPU-intensive    |
| GPU               | ml.p3._, ml.g4dn._ | Deep learning    |
| Memory Optimized  | ml.r5.\*           | Large datasets   |

## Training Modes

### File Mode

- Data downloaded to instance
- Best for iterative access
- Default mode

### Pipe Mode

- Data streamed from S3
- No download wait time
- Best for large datasets

### FastFile Mode

- POSIX-compliant access
- Lazy loading
- Best for random access patterns

## Distributed Training

### Data Parallelism

Split data across instances, each has full model copy.

```python
from sagemaker.pytorch import PyTorch

estimator = PyTorch(
    entry_point="train.py",
    instance_count=4,
    instance_type="ml.p3.16xlarge",
    distribution={"smdistributed": {"dataparallel": {"enabled": True}}}
)
```

### Model Parallelism

Split model across instances for large models.

```python
distribution={
    "smdistributed": {
        "modelparallel": {
            "enabled": True,
            "parameters": {"partitions": 2}
        }
    }
}
```

## Spot Training

Save up to 90% on training costs.

```python
estimator = Estimator(
    ...
    use_spot_instances=True,
    max_wait=3600,  # Maximum wait time
    max_run=1800,   # Maximum run time
    checkpoint_s3_uri="s3://bucket/checkpoints/"
)
```

## Exam Tips

!!! warning "Key Points" - Use Pipe Mode for large datasets - Use Spot Instances with checkpointing for cost savings - Data Parallelism for scaling with batch size - Model Parallelism for models that don't fit in memory

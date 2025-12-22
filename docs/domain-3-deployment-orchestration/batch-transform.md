# Batch Transform

## Overview

Run inference on large datasets without deploying an endpoint.

## When to Use

- Large dataset inference
- No real-time requirements
- Periodic batch predictions
- Cost optimization (no always-on endpoint)

## Creating a Batch Transform Job

```python
from sagemaker.transformer import Transformer

transformer = Transformer(
    model_name="my-model",
    instance_count=2,
    instance_type="ml.m5.xlarge",
    output_path="s3://bucket/batch-output/",
    strategy="SingleRecord",  # or "MultiRecord"
    assemble_with="Line",
    max_payload=6  # MB
)

transformer.transform(
    data="s3://bucket/batch-input/",
    content_type="text/csv",
    split_type="Line"
)

transformer.wait()
```

## Configuration Options

| Parameter                 | Options                   | Description             |
| ------------------------- | ------------------------- | ----------------------- |
| strategy                  | SingleRecord, MultiRecord | How to batch records    |
| split_type                | Line, RecordIO, None      | How to split input      |
| assemble_with             | Line, None                | How to assemble output  |
| max_payload               | 0-100 MB                  | Max payload per request |
| max_concurrent_transforms | 1-100                     | Parallel processing     |

## Data Formats

### Input

```
s3://bucket/input/
├── file1.csv
├── file2.csv
└── file3.csv
```

### Output

```
s3://bucket/output/
├── file1.csv.out
├── file2.csv.out
└── file3.csv.out
```

## Batch Transform vs Endpoint

| Aspect         | Batch Transform        | Real-time Endpoint    |
| -------------- | ---------------------- | --------------------- |
| Use Case       | Large batch processing | Real-time predictions |
| Latency        | Minutes to hours       | Milliseconds          |
| Cost           | Pay per job            | Pay per hour          |
| Scaling        | Automatic              | Manual/Auto           |
| Infrastructure | Transient              | Persistent            |

## Best Practices

!!! tip "Optimization" 1. Use MultiRecord strategy for throughput 2. Increase max_concurrent_transforms for parallelism 3. Use appropriate instance types for your workload 4. Partition input data for faster processing

## Exam Tips

!!! warning "Key Points" - Batch Transform for offline, large-scale inference - No endpoint maintenance required - Cost-effective for infrequent predictions - Supports data distribution across instances

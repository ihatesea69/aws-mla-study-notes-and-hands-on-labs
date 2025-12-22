# SageMaker Instance Types

Quick reference for choosing the right instance type.

## Instance Categories

### General Purpose (ml.m5.\*)

| Instance       | vCPU | Memory | Use Case            |
| -------------- | ---- | ------ | ------------------- |
| ml.m5.large    | 2    | 8 GB   | Small jobs, testing |
| ml.m5.xlarge   | 4    | 16 GB  | Medium workloads    |
| ml.m5.2xlarge  | 8    | 32 GB  | Larger datasets     |
| ml.m5.4xlarge  | 16   | 64 GB  | Production training |
| ml.m5.12xlarge | 48   | 192 GB | Large-scale         |

**Best for**: Balanced compute and memory requirements

### Compute Optimized (ml.c5.\*)

| Instance      | vCPU | Memory | Use Case      |
| ------------- | ---- | ------ | ------------- |
| ml.c5.large   | 2    | 4 GB   | CPU-intensive |
| ml.c5.xlarge  | 4    | 8 GB   | Preprocessing |
| ml.c5.2xlarge | 8    | 16 GB  | Inference     |
| ml.c5.4xlarge | 16   | 32 GB  | Production    |

**Best for**: CPU-bound algorithms (tree-based, preprocessing)

### GPU Instances (ml.p3._, ml.p4d._, ml.g4dn._, ml.g5._)

| Instance        | GPU     | GPU Memory | Use Case                  |
| --------------- | ------- | ---------- | ------------------------- |
| ml.g4dn.xlarge  | 1x T4   | 16 GB      | Inference, light training |
| ml.g5.xlarge    | 1x A10G | 24 GB      | Training/inference        |
| ml.p3.2xlarge   | 1x V100 | 16 GB      | Deep learning training    |
| ml.p3.8xlarge   | 4x V100 | 64 GB      | Distributed training      |
| ml.p3.16xlarge  | 8x V100 | 128 GB     | Large models              |
| ml.p4d.24xlarge | 8x A100 | 320 GB     | Largest models            |

**Best for**: Deep learning, computer vision, NLP

### Memory Optimized (ml.r5.\*)

| Instance      | vCPU | Memory | Use Case             |
| ------------- | ---- | ------ | -------------------- |
| ml.r5.large   | 2    | 16 GB  | Memory-intensive     |
| ml.r5.xlarge  | 4    | 32 GB  | Large datasets       |
| ml.r5.2xlarge | 8    | 64 GB  | In-memory processing |
| ml.r5.4xlarge | 16   | 128 GB | Very large datasets  |

**Best for**: Large datasets that need to fit in memory

## Instance Selection Guide

### Training

| Algorithm Type        | Recommended        |
| --------------------- | ------------------ |
| XGBoost, linear       | ml.m5._, ml.c5._   |
| Deep learning (small) | ml.g4dn._, ml.g5._ |
| Deep learning (large) | ml.p3._, ml.p4d._  |
| Large data processing | ml.r5.\*           |

### Inference

| Workload         | Recommended                |
| ---------------- | -------------------------- |
| Low latency, CPU | ml.c5.\*                   |
| Low latency, GPU | ml.g4dn._, ml.g5._         |
| Cost-sensitive   | ml.m5.large, Serverless    |
| High throughput  | ml.c5.\* with Auto Scaling |

## Cost Optimization Tips

| Strategy      | Savings   | When to Use           |
| ------------- | --------- | --------------------- |
| Spot Training | Up to 90% | Non-urgent training   |
| Savings Plans | Up to 64% | Consistent usage      |
| Serverless    | Variable  | Unpredictable traffic |
| Right-sizing  | Varies    | Regularly             |

## Instance Limits

| Limit Type       | Default | Notes            |
| ---------------- | ------- | ---------------- |
| ml.p3 instances  | 1-2     | Request increase |
| ml.p4d instances | 0       | Request increase |
| Total instances  | Varies  | Per account      |

## Quick Decision Tree

```
Need GPU?
├── No → Need more memory than CPU?
│         ├── Yes → ml.r5.*
│         └── No → CPU-intensive?
│                   ├── Yes → ml.c5.*
│                   └── No → ml.m5.*
└── Yes → Training or Inference?
          ├── Training → Model size?
          │              ├── Small → ml.g4dn.*, ml.g5.*
          │              └── Large → ml.p3.*, ml.p4d.*
          └── Inference → ml.g4dn.xlarge
```

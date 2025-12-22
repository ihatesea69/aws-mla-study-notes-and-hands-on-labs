# Model Monitoring

## Overview

SageMaker Model Monitor detects drift and quality issues in production models.

## Monitor Types

| Type                | Description                      |
| ------------------- | -------------------------------- |
| Data Quality        | Statistical drift in input data  |
| Model Quality       | Accuracy/performance degradation |
| Bias Drift          | Changes in bias metrics          |
| Feature Attribution | Changes in feature importance    |

## Data Quality Monitoring

Detect statistical drift in input features.

```python
from sagemaker.model_monitor import DefaultModelMonitor
from sagemaker.model_monitor.dataset_format import DatasetFormat

monitor = DefaultModelMonitor(
    role=role,
    instance_count=1,
    instance_type="ml.m5.xlarge",
    volume_size_in_gb=20
)

# Create baseline from training data
monitor.suggest_baseline(
    baseline_dataset="s3://bucket/training-data/",
    dataset_format=DatasetFormat.csv(header=True),
    output_s3_uri="s3://bucket/baseline/"
)

# Create monitoring schedule
monitor.create_monitoring_schedule(
    monitor_schedule_name="my-monitoring-schedule",
    endpoint_input=endpoint_name,
    output_s3_uri="s3://bucket/monitoring-output/",
    statistics=monitor.baseline_statistics(),
    constraints=monitor.suggested_constraints(),
    schedule_cron_expression="cron(0 * ? * * *)"  # Hourly
)
```

## Model Quality Monitoring

Monitor prediction accuracy with ground truth.

```python
from sagemaker.model_monitor import ModelQualityMonitor

model_monitor = ModelQualityMonitor(
    role=role,
    instance_count=1,
    instance_type="ml.m5.xlarge"
)

# Create baseline
model_monitor.suggest_baseline(
    baseline_dataset="s3://bucket/predictions/",
    dataset_format=DatasetFormat.csv(),
    output_s3_uri="s3://bucket/model-quality-baseline/",
    problem_type="BinaryClassification",
    inference_attribute="prediction",
    ground_truth_attribute="label"
)
```

## Ground Truth Collection

```python
from sagemaker.model_monitor import GroundTruthInput

# Merge ground truth with predictions
monitor.create_monitoring_schedule(
    ...
    ground_truth_input=GroundTruthInput(
        ground_truth_s3_uri="s3://bucket/ground-truth/"
    )
)
```

## CloudWatch Integration

Model Monitor publishes metrics to CloudWatch.

```python
# Create alarm for violations
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName="DataDriftAlarm",
    MetricName="feature_baseline_drift_age",
    Namespace="aws/sagemaker/Endpoints/data-metrics",
    Statistic="Maximum",
    Period=3600,
    EvaluationPeriods=1,
    Threshold=0.5,
    ComparisonOperator="GreaterThanThreshold",
    AlarmActions=[sns_topic_arn]
)
```

## Exam Tips

!!! warning "Key Points" - Data Quality: Input feature drift detection - Model Quality: Requires ground truth labels - Bias Drift: Uses Clarify bias metrics - Feature Attribution: SHAP value changes - All monitors integrate with CloudWatch

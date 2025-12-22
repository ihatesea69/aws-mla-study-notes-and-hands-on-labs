# Lab 06: Model Monitoring

**Domain**: 4 - Monitoring & Security  
**Difficulty**: Medium  
**Time**: 60 minutes

## Objective

Set up SageMaker Model Monitor to detect data drift in production.

## Prerequisites

- Deployed endpoint (from Lab 04)
- Baseline data

## Steps

### Step 1: Create Baseline

```python
from sagemaker.model_monitor import DefaultModelMonitor
from sagemaker.model_monitor.dataset_format import DatasetFormat

# Create monitor
monitor = DefaultModelMonitor(
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    volume_size_in_gb=20,
    max_runtime_in_seconds=3600
)

# Create baseline from training data
baseline_job = monitor.suggest_baseline(
    baseline_dataset=f's3://{bucket}/{prefix}/train/train.csv',
    dataset_format=DatasetFormat.csv(header=False),
    output_s3_uri=f's3://{bucket}/{prefix}/baseline/',
    wait=True
)
```

### Step 2: Examine Baseline

```python
# Get baseline statistics
baseline_stats = monitor.baseline_statistics()
print(baseline_stats.body_dict)

# Get baseline constraints
baseline_constraints = monitor.suggested_constraints()
print(baseline_constraints.body_dict)
```

### Step 3: Enable Data Capture

```python
from sagemaker.model_monitor import DataCaptureConfig

data_capture_config = DataCaptureConfig(
    enable_capture=True,
    sampling_percentage=100,
    destination_s3_uri=f's3://{bucket}/{prefix}/data-capture/',
    capture_options=["REQUEST", "RESPONSE"]
)

# Update endpoint with data capture
predictor.update_data_capture_config(data_capture_config)
```

### Step 4: Create Monitoring Schedule

```python
from sagemaker.model_monitor import CronExpressionGenerator

monitor.create_monitoring_schedule(
    monitor_schedule_name='my-monitoring-schedule',
    endpoint_input=endpoint_name,
    output_s3_uri=f's3://{bucket}/{prefix}/monitoring-output/',
    statistics=baseline_stats,
    constraints=baseline_constraints,
    schedule_cron_expression=CronExpressionGenerator.hourly()
)
```

### Step 5: Generate Traffic and Check Results

```python
import time
import numpy as np

# Generate some predictions
for i in range(100):
    test_data = np.random.rand(1, 8)
    predictor.predict(test_data)

# Wait for monitoring execution
print("Waiting for monitoring execution...")
time.sleep(3600)  # Wait 1 hour for scheduled execution

# Check monitoring results
executions = monitor.list_executions()
latest_execution = executions[-1]
print(f"Status: {latest_execution.describe()['ProcessingJobStatus']}")
```

### Step 6: Create CloudWatch Alarm

```python
cloudwatch = boto3.client('cloudwatch')

cloudwatch.put_metric_alarm(
    AlarmName='DataDriftAlarm',
    AlarmDescription='Alert when data drift detected',
    MetricName='feature_baseline_drift_violation',
    Namespace='aws/sagemaker/Endpoints/data-metrics',
    Dimensions=[
        {'Name': 'Endpoint', 'Value': endpoint_name},
        {'Name': 'MonitoringSchedule', 'Value': 'my-monitoring-schedule'}
    ],
    Statistic='Sum',
    Period=3600,
    EvaluationPeriods=1,
    Threshold=1,
    ComparisonOperator='GreaterThanOrEqualTo',
    AlarmActions=[sns_topic_arn]
)
```

## Verification

- Baseline statistics generated
- Monitoring schedule running
- Data capture enabled
- CloudWatch alarm configured

## Cleanup

```python
# Stop monitoring schedule
monitor.stop_monitoring_schedule()
monitor.delete_monitoring_schedule()

# Delete endpoint
predictor.delete_endpoint()
```

## Key Takeaways

!!! note "Exam Points" - Baseline is created from training data - Data capture records endpoint traffic - Monitoring schedule runs periodically - Violations trigger CloudWatch metrics - Integrate with SNS for alerts

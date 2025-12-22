# CloudWatch Logging

## Overview

Monitor ML infrastructure with CloudWatch and CloudTrail.

## Amazon CloudWatch

### Key Metrics for SageMaker

| Metric                 | Description           |
| ---------------------- | --------------------- |
| Invocations            | Number of requests    |
| InvocationsPerInstance | Requests per instance |
| ModelLatency           | Inference time        |
| OverheadLatency        | SageMaker overhead    |
| Invocation4XXErrors    | Client errors         |
| Invocation5XXErrors    | Server errors         |
| CPUUtilization         | CPU usage             |
| MemoryUtilization      | Memory usage          |
| GPUUtilization         | GPU usage             |
| DiskUtilization        | Disk usage            |

### Creating Dashboards

```python
import boto3

cloudwatch = boto3.client("cloudwatch")

cloudwatch.put_dashboard(
    DashboardName="ML-Monitoring",
    DashboardBody=json.dumps({
        "widgets": [
            {
                "type": "metric",
                "properties": {
                    "title": "Invocations",
                    "metrics": [
                        ["AWS/SageMaker", "Invocations", "EndpointName", "my-endpoint"]
                    ],
                    "period": 60
                }
            },
            {
                "type": "metric",
                "properties": {
                    "title": "Latency",
                    "metrics": [
                        ["AWS/SageMaker", "ModelLatency", "EndpointName", "my-endpoint"]
                    ],
                    "period": 60
                }
            }
        ]
    })
)
```

### Creating Alarms

```python
cloudwatch.put_metric_alarm(
    AlarmName="HighLatency",
    MetricName="ModelLatency",
    Namespace="AWS/SageMaker",
    Dimensions=[{"Name": "EndpointName", "Value": "my-endpoint"}],
    Statistic="Average",
    Period=300,
    EvaluationPeriods=2,
    Threshold=1000000,  # microseconds
    ComparisonOperator="GreaterThanThreshold",
    AlarmActions=[sns_topic_arn]
)
```

## CloudWatch Logs

### SageMaker Log Groups

| Log Group                     | Contents          |
| ----------------------------- | ----------------- |
| /aws/sagemaker/TrainingJobs   | Training output   |
| /aws/sagemaker/Endpoints      | Inference logs    |
| /aws/sagemaker/ProcessingJobs | Processing output |

### Log Insights Queries

```sql
-- Find errors in last hour
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100

-- Latency percentiles
stats percentile(@duration, 50) as p50,
      percentile(@duration, 99) as p99
by bin(1h)
```

## AWS CloudTrail

Audit API calls for compliance.

### Key Events

| Event             | Description        |
| ----------------- | ------------------ |
| CreateEndpoint    | Endpoint creation  |
| DeleteEndpoint    | Endpoint deletion  |
| UpdateEndpoint    | Endpoint updates   |
| CreateTrainingJob | Training job start |
| InvokeEndpoint    | Inference calls    |

### Example Query

```sql
SELECT eventTime, eventName, userIdentity.userName, errorCode
FROM cloudtrail_logs
WHERE eventSource = 'sagemaker.amazonaws.com'
  AND eventTime > '2024-01-01'
ORDER BY eventTime DESC
```

## Exam Tips

!!! warning "Key Points" - CloudWatch Metrics: Performance monitoring - CloudWatch Logs: Application logging - CloudWatch Alarms: Automated alerting - CloudTrail: API audit logging - Use Log Insights for querying logs

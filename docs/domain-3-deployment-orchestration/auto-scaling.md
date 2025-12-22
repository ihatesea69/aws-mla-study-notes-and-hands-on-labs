# Auto Scaling

## Overview

Automatically adjust endpoint capacity based on demand.

## Application Auto Scaling

SageMaker uses Application Auto Scaling for endpoints.

### Target Tracking Scaling

Scale based on a target metric.

```python
import boto3

asg_client = boto3.client("application-autoscaling")

# Register scalable target
asg_client.register_scalable_target(
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/my-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    MinCapacity=1,
    MaxCapacity=10
)

# Create scaling policy
asg_client.put_scaling_policy(
    PolicyName="target-tracking-policy",
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/my-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    PolicyType="TargetTrackingScaling",
    TargetTrackingScalingPolicyConfiguration={
        "TargetValue": 70.0,
        "PredefinedMetricSpecification": {
            "PredefinedMetricType": "SageMakerVariantInvocationsPerInstance"
        },
        "ScaleInCooldown": 300,
        "ScaleOutCooldown": 60
    }
)
```

### Step Scaling

Scale in steps based on alarm thresholds.

```python
asg_client.put_scaling_policy(
    PolicyName="step-scaling-policy",
    ServiceNamespace="sagemaker",
    ResourceId="endpoint/my-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    PolicyType="StepScaling",
    StepScalingPolicyConfiguration={
        "AdjustmentType": "ChangeInCapacity",
        "StepAdjustments": [
            {"MetricIntervalLowerBound": 0, "MetricIntervalUpperBound": 50, "ScalingAdjustment": 1},
            {"MetricIntervalLowerBound": 50, "ScalingAdjustment": 2}
        ],
        "Cooldown": 60
    }
)
```

## Scaling Metrics

| Metric                 | Description                      |
| ---------------------- | -------------------------------- |
| InvocationsPerInstance | Average invocations per instance |
| CPUUtilization         | CPU usage percentage             |
| MemoryUtilization      | Memory usage percentage          |
| GPUUtilization         | GPU usage percentage             |
| DiskUtilization        | Disk usage percentage            |

## Cooldown Periods

| Type      | Description                  | Typical Value |
| --------- | ---------------------------- | ------------- |
| Scale Out | Wait after adding capacity   | 60 seconds    |
| Scale In  | Wait after removing capacity | 300 seconds   |

## Scheduled Scaling

Scale based on known patterns.

```python
asg_client.put_scheduled_action(
    ServiceNamespace="sagemaker",
    ScheduledActionName="scale-up-morning",
    ResourceId="endpoint/my-endpoint/variant/AllTraffic",
    ScalableDimension="sagemaker:variant:DesiredInstanceCount",
    Schedule="cron(0 8 * * ? *)",  # 8 AM daily
    ScalableTargetAction={
        "MinCapacity": 5,
        "MaxCapacity": 20
    }
)
```

## Best Practices

!!! tip "Scaling Optimization" 1. Use target tracking for simplicity 2. Set appropriate cooldown periods 3. Monitor CloudWatch metrics 4. Test scaling behavior before production 5. Consider scheduled scaling for predictable traffic

## Exam Tips

!!! warning "Key Points" - Target tracking is simplest approach - InvocationsPerInstance common metric - Scale out cooldown < Scale in cooldown - Scheduled scaling for predictable patterns

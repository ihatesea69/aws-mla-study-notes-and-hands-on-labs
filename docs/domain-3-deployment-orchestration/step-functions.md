# Step Functions

## Overview

Serverless workflow orchestration for ML and data pipelines.

## Key Features

- Visual workflow designer
- Native AWS service integrations
- Error handling and retries
- Parallel execution
- Human approval steps

## State Types

| State        | Description                            |
| ------------ | -------------------------------------- |
| Task         | Execute work (Lambda, SageMaker, etc.) |
| Choice       | Conditional branching                  |
| Parallel     | Concurrent execution                   |
| Map          | Iterate over items                     |
| Wait         | Pause execution                        |
| Pass         | Pass input to output                   |
| Succeed/Fail | Terminal states                        |

## SageMaker Integration

```json
{
  "Comment": "ML Training Pipeline",
  "StartAt": "CreateTrainingJob",
  "States": {
    "CreateTrainingJob": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sagemaker:createTrainingJob.sync",
      "Parameters": {
        "TrainingJobName.$": "$$.Execution.Name",
        "AlgorithmSpecification": {
          "TrainingImage": "image-uri",
          "TrainingInputMode": "File"
        },
        "RoleArn": "arn:aws:iam::account:role/SageMakerRole",
        "InputDataConfig": [
          {
            "ChannelName": "train",
            "DataSource": {
              "S3DataSource": {
                "S3Uri": "s3://bucket/train/"
              }
            }
          }
        ],
        "OutputDataConfig": {
          "S3OutputPath": "s3://bucket/output/"
        },
        "ResourceConfig": {
          "InstanceCount": 1,
          "InstanceType": "ml.m5.large",
          "VolumeSizeInGB": 50
        }
      },
      "Next": "CreateModel"
    },
    "CreateModel": {
      "Type": "Task",
      "Resource": "arn:aws:states:::sagemaker:createModel",
      "Parameters": {
        "ModelName.$": "$$.Execution.Name",
        "PrimaryContainer": {
          "Image": "inference-image",
          "ModelDataUrl.$": "$.ModelArtifacts.S3ModelArtifacts"
        },
        "ExecutionRoleArn": "role-arn"
      },
      "End": true
    }
  }
}
```

## Error Handling

```json
{
  "Type": "Task",
  "Resource": "...",
  "Retry": [
    {
      "ErrorEquals": ["States.TaskFailed"],
      "IntervalSeconds": 30,
      "MaxAttempts": 3,
      "BackoffRate": 2.0
    }
  ],
  "Catch": [
    {
      "ErrorEquals": ["States.ALL"],
      "ResultPath": "$.error",
      "Next": "HandleError"
    }
  ]
}
```

## Step Functions vs SageMaker Pipelines

| Feature       | Step Functions        | SageMaker Pipelines      |
| ------------- | --------------------- | ------------------------ |
| Focus         | General orchestration | ML-specific              |
| Integrations  | 200+ AWS services     | SageMaker-centric        |
| Caching       | No                    | Yes                      |
| ML Features   | Basic                 | Rich (lineage, registry) |
| Visual Editor | Yes                   | Limited                  |

## Exam Tips

!!! warning "When to Use" - Step Functions: Complex workflows, multi-service orchestration - SageMaker Pipelines: ML-specific, need caching/lineage - Combine both for comprehensive MLOps

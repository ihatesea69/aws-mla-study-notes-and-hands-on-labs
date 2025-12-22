# Services Comparison

Quick reference for choosing the right AWS service.

## Endpoint Types

| Type            | Latency              | Payload | Timeout | Cost Model  | Use Case         |
| --------------- | -------------------- | ------- | ------- | ----------- | ---------------- |
| Real-time       | Milliseconds         | 6 MB    | 60s     | Per hour    | Interactive apps |
| Serverless      | Seconds (cold start) | 6 MB    | 60s     | Per request | Variable traffic |
| Async           | Minutes              | 1 GB    | 15 min  | Per hour    | Large payloads   |
| Batch Transform | Hours                | -       | -       | Per job     | Offline batch    |

## Data Processing Services

| Service              | Mode      | Use Case         | Scalability    |
| -------------------- | --------- | ---------------- | -------------- |
| Glue ETL             | Batch     | Large-scale ETL  | Auto-scaling   |
| Glue DataBrew        | Batch     | Visual prep      | Managed        |
| EMR                  | Batch     | Custom Spark     | Manual/Auto    |
| Kinesis Data Streams | Streaming | Custom consumers | Shards         |
| Kinesis Firehose     | Streaming | Direct to S3/etc | Automatic      |
| SageMaker Processing | Batch     | ML data prep     | Instance-based |

## Storage for ML

| Service               | Data Type  | Access Pattern | Use Case            |
| --------------------- | ---------- | -------------- | ------------------- |
| S3                    | Any        | Object access  | Data lake, models   |
| Feature Store Online  | Features   | Low-latency    | Real-time inference |
| Feature Store Offline | Features   | Batch queries  | Training            |
| Redshift              | Structured | SQL queries    | Analytics           |
| DynamoDB              | Key-value  | Low-latency    | Application data    |

## MLOps Orchestration

| Service             | Focus       | Best For                       |
| ------------------- | ----------- | ------------------------------ |
| SageMaker Pipelines | ML-specific | End-to-end ML workflows        |
| Step Functions      | General     | Multi-service orchestration    |
| MWAA (Airflow)      | General     | Complex DAGs, existing Airflow |
| EventBridge         | Events      | Event-driven triggers          |

## Hyperparameter Tuning Strategies

| Strategy  | Best For      | Speed  | Quality  |
| --------- | ------------- | ------ | -------- |
| Bayesian  | Most cases    | Fast   | High     |
| Random    | Exploration   | Medium | Medium   |
| Grid      | Small space   | Slow   | Complete |
| Hyperband | Deep learning | Fast   | High     |

## Monitoring Services

| Service            | Purpose             | Data Type   |
| ------------------ | ------------------- | ----------- |
| Model Monitor      | Drift detection     | ML metrics  |
| CloudWatch Metrics | Infrastructure      | Time series |
| CloudWatch Logs    | Application logs    | Text        |
| CloudTrail         | API audit           | Events      |
| X-Ray              | Distributed tracing | Traces      |

## Security Services

| Service         | Purpose                  |
| --------------- | ------------------------ |
| IAM             | Identity and access      |
| KMS             | Encryption keys          |
| Secrets Manager | Credentials              |
| Macie           | Sensitive data discovery |
| VPC             | Network isolation        |
| Security Groups | Instance firewall        |

## AI Services vs Custom ML

| Use Case         | AI Service  | Custom (SageMaker) |
| ---------------- | ----------- | ------------------ |
| Text sentiment   | Comprehend  | Custom NLP         |
| Object detection | Rekognition | Custom CV          |
| Speech-to-text   | Transcribe  | Custom ASR         |
| Translation      | Translate   | Custom NMT         |
| Recommendations  | Personalize | Custom RecSys      |
| Forecasting      | Forecast    | Custom models      |

## Bedrock vs SageMaker

| Aspect         | Bedrock           | SageMaker         |
| -------------- | ----------------- | ----------------- |
| Model type     | Foundation models | Any ML model      |
| Training       | Fine-tuning only  | Full training     |
| Infrastructure | Serverless        | Managed instances |
| Customization  | Limited           | Full control      |
| Use case       | GenAI apps        | Custom ML         |

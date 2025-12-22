# Data Ingestion

## Overview

Data ingestion is the process of moving data from various sources into AWS for ML workloads.

## Key Services

### Amazon S3

Primary storage for ML data. Key concepts:

- Storage classes: Standard, Intelligent-Tiering, Glacier
- Versioning for data lineage
- S3 Select for querying data in place
- Transfer Acceleration for faster uploads

### Amazon Kinesis

Real-time streaming data ingestion.

| Service                | Use Case                        |
| ---------------------- | ------------------------------- |
| Kinesis Data Streams   | Custom real-time processing     |
| Kinesis Data Firehose  | Managed delivery to S3/Redshift |
| Kinesis Data Analytics | SQL on streaming data           |

### AWS Glue

Serverless ETL and data cataloging.

- **Crawlers**: Automatically discover schema
- **Data Catalog**: Centralized metadata repository
- **ETL Jobs**: Transform data with Spark

### AWS DataSync

Automated data transfer from on-premises to AWS.

## Best Practices

!!! tip "Data Organization"
Use a consistent folder structure in S3:
`    s3://bucket/
    ├── raw/              # Original data
    ├── processed/        # Cleaned data
    ├── features/         # Feature store data
    └── models/           # Trained models
   `

## Exam Tips

!!! warning "Common Exam Scenarios" - Streaming data → Kinesis Data Firehose to S3 - On-premises large datasets → DataSync - Schema discovery → Glue Crawlers - Cross-region replication → S3 Replication

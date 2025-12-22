# Data Storage

## Overview

Choosing the right storage solutions for ML data.

## Amazon S3

Primary data lake storage for ML.

### Storage Classes

| Class                | Use Case                | Retrieval        |
| -------------------- | ----------------------- | ---------------- |
| Standard             | Frequent access         | Immediate        |
| Intelligent-Tiering  | Unknown access patterns | Automatic        |
| Standard-IA          | Infrequent access       | Immediate        |
| Glacier              | Archive                 | Minutes to hours |
| Glacier Deep Archive | Long-term archive       | Hours            |

### S3 for ML Best Practices

- Use Parquet/ORC for columnar analytics
- Enable versioning for data lineage
- Use S3 Select for filtering at source
- Configure lifecycle policies for cost optimization

## AWS Lake Formation

Centralized data lake management.

### Key Features

- Fine-grained access control
- Data sharing across accounts
- Built-in data catalog integration
- Row/column-level security

```python
# Grant permissions
lake_formation.grant_permissions(
    Principal={'DataLakePrincipalIdentifier': 'arn:aws:iam::account:role/role'},
    Resource={'Table': {'DatabaseName': 'db', 'Name': 'table'}},
    Permissions=['SELECT']
)
```

## Amazon Athena

Serverless SQL queries on S3 data.

```sql
-- Query data directly in S3
SELECT customer_id, COUNT(*) as order_count
FROM orders
WHERE order_date >= '2024-01-01'
GROUP BY customer_id
```

### Athena for ML

- Query training data without loading into memory
- Create datasets from complex joins
- Partition data for efficient queries

## Data Formats Comparison

| Format   | Best For            | Compression | Schema   |
| -------- | ------------------- | ----------- | -------- |
| Parquet  | Analytics, columnar | High        | Embedded |
| CSV      | Simple data         | Low         | External |
| JSON     | Semi-structured     | Medium      | Flexible |
| Avro     | Streaming           | Medium      | Embedded |
| RecordIO | SageMaker           | Medium      | External |

## Exam Tips

!!! warning "Storage Decisions" - S3 + Athena for ad-hoc queries - Lake Formation for governed data access - Parquet for most ML workloads - RecordIO for large-scale SageMaker training

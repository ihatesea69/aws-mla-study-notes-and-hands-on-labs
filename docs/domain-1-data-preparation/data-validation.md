# Data Validation

## Overview

Ensuring data quality and integrity before ML training.

## AWS Glue Data Quality

Built-in data quality rules in AWS Glue.

### Rule Types

| Rule Type    | Example                       |
| ------------ | ----------------------------- |
| Completeness | Column has no null values     |
| Uniqueness   | Column values are unique      |
| Validity     | Values match expected pattern |
| Consistency  | Cross-column validation       |

### Example Rules

```python
# Glue Data Quality ruleset
rules = """
Rules = [
    ColumnExists "customer_id",
    IsComplete "customer_id",
    Uniqueness "customer_id" > 0.99,
    ColumnValues "age" between 0 and 120,
    ColumnLength "email" > 5
]
"""
```

## SageMaker Data Wrangler

Visual data preparation with built-in quality checks.

- Data profiling and visualization
- Anomaly detection
- Custom validation rules
- Export to SageMaker pipelines

## Best Practices

!!! tip "Data Quality Checklist" 1. Check for missing values and decide handling strategy 2. Validate data types match expectations 3. Check for outliers and anomalies 4. Verify data distributions are as expected 5. Ensure target variable is balanced (if classification)

## Schema Validation

Use AWS Glue Schema Registry for schema enforcement.

```python
# Register schema
from aws_glue_schema_registry import GlueSchemaRegistrySerializer

serializer = GlueSchemaRegistrySerializer(
    registry_name="my-registry",
    schema_name="my-schema"
)
```

## Exam Tips

!!! warning "Key Points" - Use Glue Data Quality for automated rule-based validation - SageMaker Data Wrangler for visual exploration and validation - Schema Registry for schema evolution and validation

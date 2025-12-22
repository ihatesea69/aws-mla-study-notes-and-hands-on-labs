# Feature Engineering

## Overview

Creating and managing features for ML models.

## SageMaker Feature Store

Centralized repository for ML features.

### Store Types

| Type          | Use Case            | Latency      |
| ------------- | ------------------- | ------------ |
| Online Store  | Real-time inference | Milliseconds |
| Offline Store | Batch training      | Minutes      |

### Creating a Feature Group

```python
from sagemaker.feature_store.feature_group import FeatureGroup

feature_group = FeatureGroup(
    name="customer-features",
    sagemaker_session=sagemaker_session,
    feature_definitions=[
        FeatureDefinition(feature_name="customer_id", feature_type=FeatureTypeEnum.STRING),
        FeatureDefinition(feature_name="age", feature_type=FeatureTypeEnum.INTEGRAL),
        FeatureDefinition(feature_name="total_purchases", feature_type=FeatureTypeEnum.FRACTIONAL),
    ]
)

feature_group.create(
    s3_uri="s3://bucket/feature-store/",
    record_identifier_name="customer_id",
    event_time_feature_name="event_time",
    role_arn=role,
    enable_online_store=True
)
```

### Ingesting Features

```python
# Ingest records
feature_group.ingest(data_frame=df, max_workers=3)
```

### Retrieving Features

```python
# Online store - real-time
record = feature_group.get_record(record_identifier_value_as_string="customer_123")

# Offline store - batch
query = feature_group.athena_query()
query.run(query_string="SELECT * FROM customer_features", output_location="s3://bucket/query-results/")
df = query.as_dataframe()
```

## Common Feature Engineering Techniques

### Numerical Features

- Normalization (min-max scaling)
- Standardization (z-score)
- Log transformation
- Binning/discretization

### Categorical Features

- One-hot encoding
- Label encoding
- Target encoding
- Embedding (for high cardinality)

### Text Features

- TF-IDF
- Word embeddings (Word2Vec, BERT)
- N-grams

### Time Series Features

- Lag features
- Rolling statistics
- Seasonal decomposition

## Exam Tips

!!! warning "Feature Store Key Points" - Online store for low-latency inference - Offline store for training data - Feature groups organize related features - Point-in-time queries prevent data leakage

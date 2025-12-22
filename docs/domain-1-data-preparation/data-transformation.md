# Data Transformation

## Overview

Transforming raw data into formats suitable for ML model training.

## Key Services

### AWS Glue ETL

Serverless Apache Spark for data transformation.

```python
# Example Glue ETL script
import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

# Read from Data Catalog
datasource = glueContext.create_dynamic_frame.from_catalog(
    database="mydb",
    table_name="mytable"
)

# Apply transformations
transformed = ApplyMapping.apply(
    frame=datasource,
    mappings=[
        ("old_col", "string", "new_col", "string"),
    ]
)

# Write to S3
glueContext.write_dynamic_frame.from_options(
    frame=transformed,
    connection_type="s3",
    connection_options={"path": "s3://bucket/output/"},
    format="parquet"
)
```

### AWS Glue DataBrew

Visual data preparation tool for non-coders.

- 250+ built-in transformations
- Profile data quality
- Recipe-based transformations

### Amazon EMR

Managed Hadoop/Spark for large-scale processing.

| Use Case | When to Use                          |
| -------- | ------------------------------------ |
| Glue     | Serverless, simple ETL               |
| EMR      | Complex processing, custom libraries |
| DataBrew | Visual, no-code preparation          |

### SageMaker Processing

Run data processing jobs with custom containers.

```python
from sagemaker.processing import ScriptProcessor

processor = ScriptProcessor(
    role=role,
    image_uri=image_uri,
    instance_count=1,
    instance_type="ml.m5.xlarge"
)

processor.run(
    code="preprocessing.py",
    inputs=[ProcessingInput(source="s3://input/", destination="/opt/ml/processing/input")],
    outputs=[ProcessingOutput(source="/opt/ml/processing/output", destination="s3://output/")]
)
```

## Common Transformations

- Handling missing values
- Encoding categorical variables (one-hot, label encoding)
- Feature scaling (normalization, standardization)
- Text tokenization and vectorization
- Image resizing and augmentation

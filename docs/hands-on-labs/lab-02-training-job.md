# Lab 02: SageMaker Training Job

**Domain**: 2 - Model Development  
**Difficulty**: Medium  
**Time**: 45 minutes

## Objective

Train a model using SageMaker built-in XGBoost algorithm.

## Prerequisites

- AWS CLI configured
- Python with boto3 and sagemaker SDK
- S3 bucket for data and output

## Steps

### Step 1: Prepare Data

```python
import boto3
import sagemaker
import pandas as pd
from sklearn.model_selection import train_test_split

# Download sample data
!wget https://raw.githubusercontent.com/aws/amazon-sagemaker-examples/main/introduction_to_amazon_algorithms/xgboost_abalone/abalone.csv

# Load and prepare
df = pd.read_csv('abalone.csv', header=None)

# Split data
train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)
train_df, val_df = train_test_split(train_df, test_size=0.2, random_state=42)

# Save to CSV (target column first for XGBoost)
train_df.to_csv('train.csv', index=False, header=False)
val_df.to_csv('validation.csv', index=False, header=False)
test_df.to_csv('test.csv', index=False, header=False)
```

### Step 2: Upload to S3

```python
sagemaker_session = sagemaker.Session()
bucket = sagemaker_session.default_bucket()
prefix = 'xgboost-abalone'

train_path = sagemaker_session.upload_data('train.csv', bucket=bucket, key_prefix=f'{prefix}/train')
val_path = sagemaker_session.upload_data('validation.csv', bucket=bucket, key_prefix=f'{prefix}/validation')
```

### Step 3: Configure Training Job

```python
from sagemaker import image_uris
from sagemaker.estimator import Estimator

# Get XGBoost container
region = sagemaker_session.boto_region_name
xgb_image = image_uris.retrieve('xgboost', region, version='1.5-1')

# Get execution role
role = sagemaker.get_execution_role()

# Create estimator
xgb_estimator = Estimator(
    image_uri=xgb_image,
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    output_path=f's3://{bucket}/{prefix}/output',
    sagemaker_session=sagemaker_session
)

# Set hyperparameters
xgb_estimator.set_hyperparameters(
    objective='reg:squarederror',
    num_round=100,
    max_depth=5,
    eta=0.1,
    subsample=0.8,
    colsample_bytree=0.8
)
```

### Step 4: Start Training

```python
from sagemaker.inputs import TrainingInput

train_input = TrainingInput(train_path, content_type='text/csv')
val_input = TrainingInput(val_path, content_type='text/csv')

xgb_estimator.fit({
    'train': train_input,
    'validation': val_input
})
```

### Step 5: Verify Training

```python
# Check training job status
training_job_name = xgb_estimator.latest_training_job.name
print(f"Training job: {training_job_name}")

# Model artifact location
model_artifact = xgb_estimator.model_data
print(f"Model artifact: {model_artifact}")
```

## Verification

- Training job completed successfully
- Model artifact saved to S3
- Training metrics available in CloudWatch

## Cleanup

```python
# Delete training artifacts (optional)
import boto3
s3 = boto3.resource('s3')
bucket_obj = s3.Bucket(bucket)
bucket_obj.objects.filter(Prefix=prefix).delete()
```

## Key Takeaways

!!! note "Exam Points" - XGBoost expects target column first - Use TrainingInput for data channels - Model artifacts saved to S3 automatically - Training logs available in CloudWatch

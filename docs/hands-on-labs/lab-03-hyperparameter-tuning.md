# Lab 03: Hyperparameter Tuning

**Domain**: 2 - Model Development  
**Difficulty**: Medium  
**Time**: 60 minutes

## Objective

Use SageMaker Automatic Model Tuning to find optimal hyperparameters.

## Prerequisites

- Completed Lab 02 (training data in S3)
- SageMaker execution role

## Steps

### Step 1: Define Hyperparameter Ranges

```python
from sagemaker.tuner import (
    HyperparameterTuner,
    ContinuousParameter,
    IntegerParameter,
    CategoricalParameter
)

hyperparameter_ranges = {
    'eta': ContinuousParameter(0.01, 0.3),
    'max_depth': IntegerParameter(3, 10),
    'subsample': ContinuousParameter(0.5, 1.0),
    'colsample_bytree': ContinuousParameter(0.5, 1.0),
    'num_round': IntegerParameter(50, 200)
}
```

### Step 2: Configure Tuner

```python
objective_metric_name = 'validation:rmse'

tuner = HyperparameterTuner(
    estimator=xgb_estimator,
    objective_metric_name=objective_metric_name,
    hyperparameter_ranges=hyperparameter_ranges,
    objective_type='Minimize',
    max_jobs=10,
    max_parallel_jobs=2,
    strategy='Bayesian',
    early_stopping_type='Auto'
)
```

### Step 3: Start Tuning Job

```python
tuner.fit({
    'train': train_input,
    'validation': val_input
})

# Wait for completion
tuner.wait()
```

### Step 4: Analyze Results

```python
# Get tuning job results
tuner_analytics = tuner.analytics()

# Best training job
best_job = tuner.best_training_job()
print(f"Best job: {best_job}")

# All jobs summary
df_results = tuner_analytics.dataframe()
print(df_results.sort_values('FinalObjectiveValue').head())
```

### Step 5: Deploy Best Model

```python
# Deploy the best model
predictor = tuner.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large',
    endpoint_name='xgb-tuned-endpoint'
)
```

## Verification

- Tuning job completed with 10 training jobs
- Best hyperparameters identified
- Objective metric improved from baseline

## Cleanup

```python
# Delete endpoint
predictor.delete_endpoint()

# Delete endpoint config
sm_client = boto3.client('sagemaker')
sm_client.delete_endpoint_config(EndpointConfigName='xgb-tuned-endpoint')
```

## Key Takeaways

!!! note "Exam Points" - Bayesian strategy is most efficient for most cases - Early stopping reduces wasted compute - max_parallel_jobs affects speed and cost - Analytics provides insights into hyperparameter importance

# Lab 01: SageMaker Data Wrangler

**Domain**: 1 - Data Preparation  
**Difficulty**: Easy  
**Time**: 30 minutes

## Objective

Learn to use SageMaker Data Wrangler for visual data preparation and feature engineering.

## Prerequisites

- SageMaker Studio access
- Sample dataset (CSV)

## Steps

### Step 1: Access Data Wrangler

1. Open SageMaker Studio
2. From the launcher, select "New data flow"
3. Name your flow: `customer-churn-prep`

### Step 2: Import Data

1. Click "Import data"
2. Select "Amazon S3"
3. Navigate to your dataset or use a sample:
   ```
   s3://sagemaker-sample-files/datasets/tabular/synthetic/churn.csv
   ```
4. Click "Import"

### Step 3: Explore Data

1. Click on the dataset node
2. Select "Add analysis"
3. Choose "Table summary" to view statistics
4. Create a "Histogram" for numerical columns

### Step 4: Add Transformations

1. Click "+" after the data node
2. Select "Add transform"
3. Apply these transformations:
   - **Handle missing**: Fill missing values
   - **Encode categorical**: One-hot encode `State`
   - **Drop columns**: Remove `Phone`
   - **Custom transform**: Create new feature

```python
# Custom Pandas transform
df['HighUsage'] = (df['Day Mins'] > df['Day Mins'].median()).astype(int)
```

### Step 5: Export Flow

1. Click "Export"
2. Choose export destination:
   - "Export to S3" for data
   - "Export to Pipeline" for automation
   - "Export to Python code" for reuse

## Verification

- Transformed dataset exported to S3
- Data quality improved (no missing values)
- Features properly encoded

## Cleanup

1. Close Data Wrangler flow
2. Delete exported files if not needed
3. Stop Studio instance

## Key Takeaways

!!! note "Exam Points" - Data Wrangler is visual, no-code data preparation - Supports 300+ built-in transformations - Can export to Pipelines for automation - Part of SageMaker Studio

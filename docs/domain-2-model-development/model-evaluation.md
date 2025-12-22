# Model Evaluation

## Overview

Evaluating model performance and detecting bias.

## Classification Metrics

| Metric    | Formula               | Use When                 |
| --------- | --------------------- | ------------------------ |
| Accuracy  | (TP+TN)/(TP+TN+FP+FN) | Balanced classes         |
| Precision | TP/(TP+FP)            | False positives costly   |
| Recall    | TP/(TP+FN)            | False negatives costly   |
| F1 Score  | 2*(P*R)/(P+R)         | Balance precision/recall |
| AUC-ROC   | Area under ROC curve  | Ranking ability          |

## Regression Metrics

| Metric | Description                    |
| ------ | ------------------------------ |
| MSE    | Mean Squared Error             |
| RMSE   | Root Mean Squared Error        |
| MAE    | Mean Absolute Error            |
| R²     | Coefficient of determination   |
| MAPE   | Mean Absolute Percentage Error |

## SageMaker Clarify

Detect bias and explain predictions.

### Bias Detection

```python
from sagemaker.clarify import SageMakerClarifyProcessor, BiasConfig, DataConfig

clarify_processor = SageMakerClarifyProcessor(
    role=role,
    instance_count=1,
    instance_type="ml.m5.xlarge"
)

bias_config = BiasConfig(
    label_values_or_threshold=[1],
    facet_name="gender",
    facet_values_or_threshold=[0]
)

data_config = DataConfig(
    s3_data_input_path="s3://bucket/data/",
    s3_output_path="s3://bucket/clarify-output/",
    label="target",
    headers=["feature1", "feature2", "target"]
)

clarify_processor.run_bias(
    data_config=data_config,
    bias_config=bias_config,
    pre_training_methods="all",
    post_training_methods="all"
)
```

### Bias Metrics

| Metric                          | Description                     |
| ------------------------------- | ------------------------------- |
| Class Imbalance (CI)            | Difference in class proportions |
| Difference in Proportions (DPL) | Label distribution difference   |
| Disparate Impact (DI)           | Ratio of positive outcomes      |

### Model Explainability

SHAP (SHapley Additive exPlanations) values.

```python
from sagemaker.clarify import ModelConfig, SHAPConfig

model_config = ModelConfig(
    model_name="my-model",
    instance_type="ml.m5.xlarge",
    instance_count=1
)

shap_config = SHAPConfig(
    baseline=[baseline_data],
    num_samples=100,
    agg_method="mean_abs"
)

clarify_processor.run_explainability(
    data_config=data_config,
    model_config=model_config,
    explainability_config=shap_config
)
```

## SageMaker Debugger

Monitor training in real-time.

- Capture tensors during training
- Built-in rules for common issues
- Profiling for performance bottlenecks

## Exam Tips

!!! warning "Key Points" - Use Clarify for bias detection and explainability - SHAP values explain individual predictions - Debugger monitors training for issues - Choose metrics based on business requirements

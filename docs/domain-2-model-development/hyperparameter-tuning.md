# Hyperparameter Tuning

## Overview

Automatic Model Tuning (AMT) in SageMaker finds optimal hyperparameters.

## Tuning Strategies

| Strategy  | Description                       | Best For           |
| --------- | --------------------------------- | ------------------ |
| Bayesian  | Probabilistic model of objective  | Most use cases     |
| Random    | Random sampling                   | Exploration        |
| Grid      | Exhaustive search                 | Small search space |
| Hyperband | Early stopping of poor performers | Large search space |

## Creating a Tuning Job

```python
from sagemaker.tuner import HyperparameterTuner, ContinuousParameter, IntegerParameter

hyperparameter_ranges = {
    "learning_rate": ContinuousParameter(0.001, 0.1),
    "num_layers": IntegerParameter(2, 10),
    "dropout": ContinuousParameter(0.1, 0.5)
}

tuner = HyperparameterTuner(
    estimator=estimator,
    objective_metric_name="validation:accuracy",
    hyperparameter_ranges=hyperparameter_ranges,
    max_jobs=20,
    max_parallel_jobs=4,
    strategy="Bayesian"
)

tuner.fit({"train": train_data, "validation": val_data})
```

## Parameter Types

| Type                 | Example                | Use Case              |
| -------------------- | ---------------------- | --------------------- |
| ContinuousParameter  | Learning rate, dropout | Floating point values |
| IntegerParameter     | Layers, neurons        | Whole numbers         |
| CategoricalParameter | Optimizer type         | Discrete choices      |

## Warm Start

Resume tuning from previous jobs.

```python
from sagemaker.tuner import WarmStartConfig, WarmStartTypes

warm_start_config = WarmStartConfig(
    warm_start_type=WarmStartTypes.TRANSFER_LEARNING,
    parents=["previous-tuning-job-name"]
)

tuner = HyperparameterTuner(
    ...
    warm_start_config=warm_start_config
)
```

## Best Practices

!!! tip "Tuning Tips" 1. Start with a wide search range 2. Use Bayesian for efficiency 3. Enable early stopping to save costs 4. Use warm start for iterative refinement

## Objective Metrics

Common metrics to optimize:

| Problem        | Metric            | Direction |
| -------------- | ----------------- | --------- |
| Classification | accuracy, f1, auc | Maximize  |
| Regression     | mse, rmse, mae    | Minimize  |
| Ranking        | ndcg              | Maximize  |

## Exam Tips

!!! warning "Key Points" - Bayesian is most efficient for most cases - Hyperband good for deep learning with early stopping - Warm start saves time when refining previous tuning - Set max_parallel_jobs based on budget and urgency

# Lab 05: SageMaker Pipelines

**Domain**: 3 - Deployment & Orchestration  
**Difficulty**: Hard  
**Time**: 90 minutes

## Objective

Build an end-to-end ML pipeline using SageMaker Pipelines.

## Prerequisites

- Training data in S3
- Understanding of SageMaker training and deployment

## Steps

### Step 1: Define Pipeline Parameters

```python
from sagemaker.workflow.parameters import (
    ParameterString,
    ParameterInteger,
    ParameterFloat
)

input_data = ParameterString(name="InputData", default_value=f"s3://{bucket}/{prefix}/data/")
instance_type = ParameterString(name="TrainingInstanceType", default_value="ml.m5.large")
model_approval_status = ParameterString(name="ModelApprovalStatus", default_value="PendingManualApproval")
```

### Step 2: Define Processing Step

```python
from sagemaker.sklearn.processing import SKLearnProcessor
from sagemaker.processing import ProcessingInput, ProcessingOutput
from sagemaker.workflow.steps import ProcessingStep

sklearn_processor = SKLearnProcessor(
    framework_version="1.0-1",
    instance_type="ml.m5.large",
    instance_count=1,
    role=role,
    sagemaker_session=sagemaker_session
)

processing_step = ProcessingStep(
    name="PreprocessData",
    processor=sklearn_processor,
    inputs=[
        ProcessingInput(source=input_data, destination="/opt/ml/processing/input")
    ],
    outputs=[
        ProcessingOutput(output_name="train", source="/opt/ml/processing/train"),
        ProcessingOutput(output_name="validation", source="/opt/ml/processing/validation"),
        ProcessingOutput(output_name="test", source="/opt/ml/processing/test")
    ],
    code="preprocessing.py"
)
```

### Step 3: Define Training Step

```python
from sagemaker.workflow.steps import TrainingStep
from sagemaker.inputs import TrainingInput

training_step = TrainingStep(
    name="TrainModel",
    estimator=xgb_estimator,
    inputs={
        "train": TrainingInput(
            s3_data=processing_step.properties.ProcessingOutputConfig.Outputs["train"].S3Output.S3Uri,
            content_type="text/csv"
        ),
        "validation": TrainingInput(
            s3_data=processing_step.properties.ProcessingOutputConfig.Outputs["validation"].S3Output.S3Uri,
            content_type="text/csv"
        )
    }
)
```

### Step 4: Define Evaluation Step

```python
from sagemaker.workflow.steps import ProcessingStep
from sagemaker.workflow.properties import PropertyFile

evaluation_report = PropertyFile(
    name="EvaluationReport",
    output_name="evaluation",
    path="evaluation.json"
)

evaluation_step = ProcessingStep(
    name="EvaluateModel",
    processor=sklearn_processor,
    inputs=[
        ProcessingInput(
            source=training_step.properties.ModelArtifacts.S3ModelArtifacts,
            destination="/opt/ml/processing/model"
        ),
        ProcessingInput(
            source=processing_step.properties.ProcessingOutputConfig.Outputs["test"].S3Output.S3Uri,
            destination="/opt/ml/processing/test"
        )
    ],
    outputs=[
        ProcessingOutput(output_name="evaluation", source="/opt/ml/processing/evaluation")
    ],
    code="evaluation.py",
    property_files=[evaluation_report]
)
```

### Step 5: Define Condition Step

```python
from sagemaker.workflow.conditions import ConditionGreaterThanOrEqualTo
from sagemaker.workflow.condition_step import ConditionStep
from sagemaker.workflow.functions import JsonGet

condition = ConditionGreaterThanOrEqualTo(
    left=JsonGet(
        step_name=evaluation_step.name,
        property_file=evaluation_report,
        json_path="metrics.accuracy.value"
    ),
    right=0.8
)
```

### Step 6: Define Register Model Step

```python
from sagemaker.workflow.model_step import ModelStep
from sagemaker.model import Model

model = Model(
    image_uri=xgb_image,
    model_data=training_step.properties.ModelArtifacts.S3ModelArtifacts,
    role=role
)

register_step = ModelStep(
    name="RegisterModel",
    step_args=model.register(
        content_types=["text/csv"],
        response_types=["text/csv"],
        inference_instances=["ml.m5.large"],
        transform_instances=["ml.m5.large"],
        model_package_group_name="my-model-group",
        approval_status=model_approval_status
    )
)
```

### Step 7: Create and Execute Pipeline

```python
from sagemaker.workflow.pipeline import Pipeline

pipeline = Pipeline(
    name="my-ml-pipeline",
    parameters=[input_data, instance_type, model_approval_status],
    steps=[processing_step, training_step, evaluation_step,
           ConditionStep(
               name="CheckAccuracy",
               conditions=[condition],
               if_steps=[register_step],
               else_steps=[]
           )]
)

# Create/update pipeline
pipeline.upsert(role_arn=role)

# Start execution
execution = pipeline.start()
execution.wait()
```

## Verification

- Pipeline created successfully
- All steps executed in order
- Model registered if accuracy threshold met

## Cleanup

```python
# Delete pipeline
pipeline.delete()
```

## Key Takeaways

!!! note "Exam Points" - Pipelines automate end-to-end ML workflows - ConditionStep gates deployment on quality - PropertyFile extracts metrics from processing output - Parameters make pipelines reusable

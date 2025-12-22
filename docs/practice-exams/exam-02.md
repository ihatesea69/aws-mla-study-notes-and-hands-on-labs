# Practice Exam 02

**Time Limit**: 170 minutes  
**Questions**: 65  
**Passing Score**: 720/1000

---

## Question 1

A data scientist needs to train an image classification model on a dataset of 1 million images. The model requires GPU acceleration. Which SageMaker instance type is MOST appropriate for this training job?

A. ml.m5.4xlarge  
B. ml.c5.4xlarge  
C. ml.p3.2xlarge  
D. ml.r5.4xlarge

<details>
<summary>Answer</summary>

**C. ml.p3.2xlarge**

P3 instances have NVIDIA V100 GPUs optimized for deep learning training. Image classification is compute-intensive and benefits significantly from GPU acceleration. M5 is general purpose, C5 is CPU compute-optimized, R5 is memory-optimized.

**Domain**: 2 - Model Development

</details>

---

## Question 2

A company has deployed a real-time endpoint but wants to reduce costs during nights and weekends when traffic is minimal. Which approach provides the BEST cost optimization while maintaining availability?

A. Delete the endpoint and recreate it when needed  
B. Use Serverless Inference instead  
C. Configure Auto Scaling with scheduled actions  
D. Reduce the instance type during off-peak hours

<details>
<summary>Answer</summary>

**C. Configure Auto Scaling with scheduled actions**

Scheduled Auto Scaling can reduce capacity during known low-traffic periods while maintaining availability. Serverless might have cold start issues. Deleting endpoints causes downtime. Instance type changes require endpoint updates.

**Domain**: 3 - Deployment and Orchestration

</details>

---

## Question 3

An ML engineer needs to validate data quality before training. They want to check for null values, unique constraints, and value ranges. Which AWS service provides built-in data quality rules?

A. SageMaker Data Wrangler  
B. AWS Glue Data Quality  
C. Amazon Macie  
D. AWS Config

<details>
<summary>Answer</summary>

**B. AWS Glue Data Quality**

Glue Data Quality provides built-in rules for completeness, uniqueness, accuracy, and custom validations. Data Wrangler is for visual data prep. Macie detects sensitive data. Config tracks resource compliance.

**Domain**: 1 - Data Preparation

</details>

---

## Question 4

A team wants to track and compare multiple training runs with different hyperparameters. They need to log metrics, parameters, and artifacts for each run. Which SageMaker feature should they use?

A. SageMaker Model Registry  
B. SageMaker Experiments  
C. SageMaker Model Monitor  
D. SageMaker Debugger

<details>
<summary>Answer</summary>

**B. SageMaker Experiments**

Experiments provides tracking for ML runs including metrics, parameters, and artifacts. It enables comparison across runs and organizing experiments. Model Registry is for versioning approved models. Model Monitor tracks production drift. Debugger analyzes training issues.

**Domain**: 2 - Model Development

</details>

---

## Question 5

A company needs to detect personally identifiable information (PII) in their ML training data stored in S3. Which AWS service should they use?

A. AWS Glue Data Quality  
B. Amazon Comprehend  
C. Amazon Macie  
D. AWS Config

<details>
<summary>Answer</summary>

**C. Amazon Macie**

Macie uses ML to automatically discover, classify, and protect sensitive data including PII in S3. Comprehend can detect PII in text but isn't designed for S3 scanning. Glue Data Quality checks data integrity. Config tracks resource compliance.

**Domain**: 4 - Monitoring and Security

</details>

---

## Question 6

An ML team needs to deploy multiple similar models (one per customer) efficiently. Each model is about 500MB and inference logic is identical. Which SageMaker deployment approach is MOST cost-effective?

A. Deploy separate endpoints for each model  
B. Use Multi-Model Endpoint  
C. Use Serverless Inference for each model  
D. Use Multi-Container Endpoint

<details>
<summary>Answer</summary>

**B. Use Multi-Model Endpoint**

Multi-Model Endpoints host multiple models on shared infrastructure, loading models dynamically. This is ideal for many similar models with sparse individual usage. Separate endpoints waste resources. Serverless has cold starts. Multi-Container is for different inference logic.

**Domain**: 3 - Deployment and Orchestration

</details>

---

## Question 7

A data engineer needs to stream real-time clickstream data from their website directly into S3 for ML processing. Which AWS service should they use?

A. Amazon Kinesis Data Streams  
B. Amazon Kinesis Data Firehose  
C. Amazon SQS  
D. Amazon SNS

<details>
<summary>Answer</summary>

**B. Amazon Kinesis Data Firehose**

Firehose automatically delivers streaming data to S3 (and other destinations) without requiring consumer code. Data Streams requires custom consumers. SQS is for message queuing. SNS is for pub/sub notifications.

**Domain**: 1 - Data Preparation

</details>

---

## Question 8

A company wants to use Claude 3 through Amazon Bedrock but needs to ensure the model doesn't generate responses about certain competitors. Which Bedrock feature should they configure?

A. Fine-tuning  
B. Knowledge Bases  
C. Guardrails  
D. Agents

<details>
<summary>Answer</summary>

**C. Guardrails**

Guardrails allows you to configure denied topics, content filters, and word filters to control model outputs. Fine-tuning changes model behavior through training. Knowledge Bases adds context. Agents automate tasks.

**Domain**: 2 - Model Development

</details>

---

## Question 9

An ML engineer needs to run a SageMaker notebook instance in a private subnet without internet access while still accessing S3 and SageMaker services. What should they configure?

A. NAT Gateway  
B. VPC Endpoints  
C. Internet Gateway  
D. AWS Direct Connect

<details>
<summary>Answer</summary>

**B. VPC Endpoints**

VPC Endpoints (Interface and Gateway) provide private connectivity to AWS services without requiring internet access. NAT and Internet Gateways provide internet access. Direct Connect is for on-premises connectivity.

**Domain**: 4 - Monitoring and Security

</details>

---

## Question 10

A company is using XGBoost for binary classification. They want to automatically find the best combination of learning rate, max depth, and number of trees. Which SageMaker feature should they use?

A. SageMaker Autopilot  
B. SageMaker Automatic Model Tuning  
C. SageMaker JumpStart  
D. SageMaker Clarify

<details>
<summary>Answer</summary>

**B. SageMaker Automatic Model Tuning**

Automatic Model Tuning (Hyperparameter Optimization) systematically searches for optimal hyperparameters. Autopilot automates the entire ML process. JumpStart provides pre-trained models. Clarify is for bias and explainability.

**Domain**: 2 - Model Development

</details>

---

_Continue adding more questions following this format..._

---

## End of Practice Exam 02

**Review your answers and study the explanations for any questions you got wrong.**

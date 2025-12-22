# Practice Exam 01

**Time Limit**: 170 minutes  
**Questions**: 65  
**Passing Score**: 720/1000

---

## Question 1

A machine learning engineer needs to deploy a model that receives thousands of inference requests per second with sub-100ms latency requirements. The traffic pattern is consistent throughout business hours. Which SageMaker deployment option should they use?

A. Serverless Inference endpoint  
B. Real-time Inference endpoint with Auto Scaling  
C. Asynchronous Inference endpoint  
D. Batch Transform job

<details>
<summary>Answer</summary>

**B. Real-time Inference endpoint with Auto Scaling**

Real-time endpoints provide consistent low-latency inference. Auto Scaling handles the high request volume. Serverless has cold start delays unsuitable for strict latency requirements. Async and Batch are not real-time solutions.

**Domain**: 3 - Deployment and Orchestration

</details>

---

## Question 2

A data scientist is preparing training data stored in Amazon S3. The dataset contains 500GB of CSV files. They need to efficiently load this data for SageMaker training. Which approach is MOST appropriate?

A. Use File mode with ml.m5.xlarge instance  
B. Use Pipe mode with RecordIO format  
C. Use FastFile mode with Parquet format  
D. Download data to local disk before training

<details>
<summary>Answer</summary>

**B. Use Pipe mode with RecordIO format**

Pipe mode streams data directly from S3, eliminating download time for large datasets. RecordIO is optimized for streaming. File mode requires downloading all data first. FastFile is good for random access but Pipe is better for sequential training access.

**Domain**: 1 - Data Preparation

</details>

---

## Question 3

A company wants to detect when their deployed fraud detection model starts receiving input data that differs significantly from training data. Which AWS service should they use?

A. Amazon CloudWatch Logs  
B. AWS CloudTrail  
C. SageMaker Model Monitor  
D. SageMaker Debugger

<details>
<summary>Answer</summary>

**C. SageMaker Model Monitor**

Model Monitor specifically detects data drift by comparing production data against baseline statistics from training data. CloudWatch Logs captures application logs. CloudTrail audits API calls. Debugger monitors training, not inference.

**Domain**: 4 - Monitoring and Security

</details>

---

## Question 4

A team needs to automate their ML workflow including data preprocessing, training, evaluation, and conditional model registration. The model should only be registered if accuracy exceeds 85%. Which service is BEST suited for this?

A. AWS Step Functions  
B. Amazon MWAA (Managed Airflow)  
C. SageMaker Pipelines  
D. AWS Glue Workflows

<details>
<summary>Answer</summary>

**C. SageMaker Pipelines**

SageMaker Pipelines is purpose-built for ML workflows with native support for conditional steps, model registration, and integration with SageMaker components. Step Functions works but lacks ML-specific features like caching and lineage. MWAA is more general-purpose. Glue is for data workflows.

**Domain**: 3 - Deployment and Orchestration

</details>

---

## Question 5

An ML engineer needs to store and manage features that will be used for both batch training and real-time inference. The same features should be available with low latency for predictions and for offline training jobs. Which solution should they use?

A. Amazon DynamoDB for online, S3 for offline  
B. SageMaker Feature Store with Online and Offline stores  
C. Amazon ElastiCache for online, Redshift for offline  
D. Amazon RDS for both online and offline

<details>
<summary>Answer</summary>

**B. SageMaker Feature Store with Online and Offline stores**

SageMaker Feature Store provides both Online store (low latency, DynamoDB-backed) and Offline store (S3-backed for training) from a single feature definition. This ensures consistency between training and inference features. Custom solutions require more management.

**Domain**: 1 - Data Preparation

</details>

---

## Question 6

A company wants to reduce their SageMaker training costs by up to 90% for non-time-critical workloads. Which approach should they implement?

A. Use smaller instance types  
B. Use Spot Training with checkpointing  
C. Use Savings Plans  
D. Reduce training epochs

<details>
<summary>Answer</summary>

**B. Use Spot Training with checkpointing**

Spot Training can reduce costs by up to 90% by using spare EC2 capacity. Checkpointing ensures training can resume if interrupted. Savings Plans offer up to 64% savings. Smaller instances may increase training time. Reducing epochs may hurt model quality.

**Domain**: 4 - Monitoring and Security (Cost Optimization)

</details>

---

## Question 7

A data engineer needs to automatically discover the schema of new data files landing in S3 and make them queryable via Athena. Which AWS Glue component should they use?

A. AWS Glue ETL Jobs  
B. AWS Glue Crawlers  
C. AWS Glue DataBrew  
D. AWS Glue Triggers

<details>
<summary>Answer</summary>

**B. AWS Glue Crawlers**

Glue Crawlers automatically scan data sources, infer schemas, and populate the Glue Data Catalog. Tables in the Data Catalog are automatically queryable by Athena. ETL Jobs transform data. DataBrew is for visual data prep. Triggers schedule jobs.

**Domain**: 1 - Data Preparation

</details>

---

## Question 8

An ML team wants to explain individual predictions from their XGBoost model to business stakeholders. They need to show which features contributed most to each prediction. Which SageMaker capability should they use?

A. SageMaker Debugger  
B. SageMaker Clarify with SHAP  
C. SageMaker Experiments  
D. SageMaker Model Monitor

<details>
<summary>Answer</summary>

**B. SageMaker Clarify with SHAP**

SageMaker Clarify provides model explainability using SHAP (SHapley Additive exPlanations) values to show feature contributions to individual predictions. Debugger monitors training. Experiments tracks runs. Model Monitor detects drift.

**Domain**: 2 - Model Development

</details>

---

## Question 9

A company is building a customer support chatbot that needs to access their internal knowledge base documents to answer questions accurately. Which Amazon Bedrock feature should they use?

A. Bedrock Agents  
B. Bedrock Fine-tuning  
C. Bedrock Knowledge Bases  
D. Bedrock Guardrails

<details>
<summary>Answer</summary>

**C. Bedrock Knowledge Bases**

Knowledge Bases implement RAG (Retrieval Augmented Generation) by connecting foundation models to your data. Documents are chunked, embedded, and stored in a vector database for retrieval. Agents automate tasks. Fine-tuning customizes models. Guardrails filter content.

**Domain**: 2 - Model Development

</details>

---

## Question 10

A machine learning engineer needs to ensure that their SageMaker training job output and model artifacts are encrypted at rest using a customer-managed key. Which AWS service should they use?

A. AWS Secrets Manager  
B. AWS Certificate Manager  
C. AWS Key Management Service (KMS)  
D. AWS CloudHSM

<details>
<summary>Answer</summary>

**C. AWS Key Management Service (KMS)**

KMS provides customer-managed encryption keys that can be specified in SageMaker training job configuration for encrypting output data and model artifacts. Secrets Manager stores credentials. Certificate Manager handles SSL/TLS. CloudHSM is for dedicated hardware security modules.

**Domain**: 4 - Monitoring and Security

</details>

---

_Continue adding more questions following this format..._

---

## Question 65

A company needs to process ML inference requests that may take up to 15 minutes to complete. Request payloads can be up to 500MB. The application can tolerate delays as results are processed asynchronously. Which SageMaker endpoint type should they use?

A. Real-time Inference  
B. Serverless Inference  
C. Asynchronous Inference  
D. Multi-Model Endpoint

<details>
<summary>Answer</summary>

**C. Asynchronous Inference**

Asynchronous Inference supports payloads up to 1GB and processing times up to 15 minutes. Results are stored in S3 and can trigger SNS notifications. Real-time and Serverless have 60-second timeouts and 6MB payload limits. Multi-Model hosts multiple models but doesn't extend timeouts.

**Domain**: 3 - Deployment and Orchestration

</details>

---

## End of Practice Exam 01

**Review your answers and study the explanations for any questions you got wrong.**

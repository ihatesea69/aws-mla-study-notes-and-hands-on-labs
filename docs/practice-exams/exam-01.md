# Practice Exam 01

!!! info "Exam Details"
    - **Total Questions**: 65
    - **Estimated Time**: ~130 minutes
    - **Passing Score**: 72%

## Question 1

An ML engineer is tuning an image classification model that shows poor performance on one of two available classes during prediction. Analysis reveals that the images whose class the model performed poorly on represent an extremely small fraction of the whole training dataset. The ML engineer must improve the model's performance. Which solution will meet this requirement?

- **A.** Optimize for accuracy. Use image augmentation on the less common images to generate new samples.
- **B.** Optimize for F1 score. Use image augmentation on the less common images to generate new samples.
- **C.** Optimize for accuracy. Use Synthetic Minority Oversampling Technique (SMOTE) on the less common images to generate new samples.
- **D.** Optimize for F1 score. Use Synthetic Minority Oversampling Technique (SMOTE) on the less common images to generate new samples.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Optimize for F1 score. Use Synthetic Minority Oversampling Technique (SMOTE) on the less common images to generate new samples. 1

---

## Question 2

An ML engineer needs to deploy ML models to get inferences from large datasets in an asynchronous manner. The ML engineer also needs to implement scheduled monitoring of the data quality of the models. The ML engineer must receive alerts when changes in data quality occur. Which solution will meet these requirements?

- **A.** Deploy the models by using scheduled AWS Glue jobs. Use Amazon CloudWatch alarms to monitor the data quality and to send alerts.
- **B.** Deploy the models by using scheduled AWS Batch jobs. Use AWS CloudTrail to monitor the data quality and to send alerts.
- **C.** Deploy the models by using Amazon Elastic Container Service (Amazon ECS) on AWS Fargate. Use Amazon EventBridge to monitor the data quality and to send alerts.
- **D.** Deploy the models by using Amazon SageMaker AI batch transform. Use SageMaker Model Monitor to monitor the data quality and to send alerts.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Deploy the models by using Amazon SageMaker AI batch transform. Use SageMaker Model Monitor to monitor the data quality and to send alerts. 2

---

## Question 3

!!! warning "Ordering - Arrange 3 Steps"

An ML engineer needs to use Amazon SageMaker to develop an ML solution for a company. The solution will use streaming video from cameras to count the number of people who walk past the company's store every day. Select and order the steps to implement the first version of the algorithm. (Select and order THREE)

- **Step 1.** Determine if the challenge is a classification, detection, or segmentation problem.
- **Step 2.** Decide the data input format and apply data augmentation if necessary.
- **Step 3.** Choose a built-in algorithm or pre-trained model.

??? success "Reveal Answer"
    **Correct Answer: 1,2,3**

    1.	Step 1: Determine if the challenge is a classification, detection, or segmentation problem. 2.	Step 2: Decide the data input format and apply data augmentation if necessary. 3.	Step 3: Choose a built-in algorithm or pre-trained model. 3

---

## Question 4

A company wants to reduce the cost of its containerized ML applications. The applications use ML models that run on Amazon EC2 instances, AWS Lambda functions, and an Amazon Elastic Container Service (Amazon ECS) cluster. The EC2 workloads and ECS workloads use Amazon Elastic Block Store (Amazon EBS) volumes to save predictions and artifacts. An ML engineer must identify resources that are being used inefficiently. The ML engineer also must generate recommendations to reduce the cost of these resources. Which solution will meet these requirements with the LEAST development effort?

- **A.** Create code to evaluate each instance's memory and compute usage.
- **B.** Add cost allocation tags to the resources. Activate the tags in AWS Billing and Cost Management.
- **C.** Check AWS CloudTrail event history for the creation of the resources.
- **D.** Run AWS Compute Optimizer.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Run AWS Compute Optimizer. 4

---

## Question 5

An ML engineer is using Amazon SageMaker AI to train an ML model. The ML engineer needs to use SageMaker AI automatic model tuning (AMT) features to tune the model hyperparameters over a large parameter space. The model has 20 categorical hyperparameters and 7 continuous hyperparameters that can be tuned. The ML engineer needs to run the tuning job a maximum of 1,000 times. The ML engineer must ensure that each parameter trial is built based on the performance of the previous trial. Which solution will meet these requirements?

- **A.** Define the search space as categorical parameters of 1,000 possible combinations. Use grid search.
- **B.** Define the search space as continuous parameters. Use random search. Set the maximum number of tuning jobs to 1,000.
- **C.** Define the search space as categorical parameters and continuous parameters. Use Bayesian optimization. Set the maximum number of training jobs to 1,000.
- **D.** Define the search space as categorical parameters and continuous parameters. Use grid search. Set the maximum number of tuning jobs to 1,000.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Define the search space as categorical parameters and continuous parameters. Use Bayesian optimization. Set the maximum number of training jobs to 1,000. 5

---

## Question 6

A company has a large, unstructured dataset. The dataset includes many duplicate records across several key attributes. Which solution on AWS will detect duplicates in the dataset with the LEAST operational overhead?

- **A.** Use Amazon Mechanical Turk jobs to detect duplicates.
- **B.** Use Amazon QuickSight ML Insights to build a custom deduplication model.
- **C.** Use Amazon SageMaker Data Wrangler to pre-process and detect duplicates.
- **D.** Use the AWS Glue FindMatches transform to detect duplicates.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Use the AWS Glue FindMatches transform to detect duplicates. 6

---

## Question 7

A hospital is using an ML model to validate x-ray results. The hospital runs a nightly batch inference job. The hospital needs to produce a daily report about model data quality and model performance. Which solution will meet these requirements?

- **A.** Schedule a monitoring job in Amazon SageMaker Model Monitor. Generate the monitoring results for the model and data.
- **B.** Create an Amazon CloudWatch dashboard that includes the metrics for processing steps in the nightly batch inference job. Compare the baseline resource metrics. Share the dashboard link.
- **C.** Use AWS Glue DataBrew to create a custom recipe job that uses the Numerical Statistics data quality check for the model file. Generate the results.
- **D.** Create a SageMaker AI pipeline that includes a Quality Check step to run monitoring jobs. Generate the monitoring results for the model and the data.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Schedule a monitoring job in Amazon SageMaker Model Monitor. Generate the monitoring results for the model and data. 7

---

## Question 8

A healthcare analytics company is developing an ML model to predict whether a patient is at risk of developing diabetes based on historical health data. The dataset the company is using is highly imbalanced and includes patient demographics, medical history, and lifestyle changes. Which solution will meet these requirements?

- **A.** Use the Amazon SageMaker AI XGBoost algorithm. Set scale_pos_weight to adjust for the imbalance in the positive class.
- **B.** Use a k-means clustering algorithm. Set k to specify the number of imbalanced clusters.
- **C.** Use the Amazon SageMaker AI DeepAR algorithm. Set epochs for the number of training iterations in the imbalanced class.
- **D.** Use the Amazon SageMaker AI Random Cut Forest (RCF) algorithm. Set a contamination hyperparameter for the anomaly imbalance in the positive class.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use the Amazon SageMaker AI XGBoost algorithm. Set scale_pos_weight to adjust for the imbalance in the positive class. 8

---

## Question 9

An ML engineer is setting up a continuous integration and continuous delivery (CI/CD) pipeline for an ML workflow in Amazon SageMaker AI. The pipeline needs to automate model re-training, testing, and deployment whenever new data is uploaded to an Amazon S3 bucket. New data files are approximately 10 GB in size. The ML engineer wants to track model versions for auditing. Which solution will meet these requirements?

- **A.** Use AWS CodePipeline, Amazon S3, and AWS CodeBuild to retrain and deploy the model automatically and to track model versions.
- **B.** Use SageMaker Pipelines with the SageMaker Model Registry to orchestrate model training and version tracking.
- **C.** Create an AWS Lambda function to re-train and deploy the model. Use Amazon EventBridge to invoke the Lambda function. Reference the Lambda logs to track model versions.
- **D.** Use SageMaker AI notebook instances to manually re-train and deploy the model when needed. Reference AWS CloudTrail logs to track model versions.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use SageMaker Pipelines with the SageMaker Model Registry to orchestrate model training and version tracking. 9

---

## Question 10

An ML engineer needs to use AWS CloudFormation to create an ML model that an Amazon SageMaker AI endpoint will host. Which resource should the ML engineer declare in the CloudFormation template to meet this requirement?

- **A.** AWS::SageMaker::Model
- **B.** AWS::SageMaker::Endpoint
- **C.** AWS::SageMaker::NotebookInstance
- **D.** AWS::SageMaker::Pipeline

??? success "Reveal Answer"
    **Correct Answer: A**

    A. AWS::SageMaker::Model 10

---

## Question 11

!!! warning "Ordering - Arrange 3 Steps"

An ML engineer needs to automate the rebuild and redeployment of an ML model. Updates will occur when changes are made to the model's code base. The ML engineer must use AWS services to configure a CI/CD pipeline. Select and order the steps to configure the CI/CD pipeline. (Select and order THREE)

- **Step 1.** Create a Git source code repository.
- **Step 2.** Create a pipeline in AWS CodePipeline. Build and test containers in AWS CodeBuild.
- **Step 3.** Invoke Amazon SageMaker Pipelines to run all steps required for model training and deployment.

??? success "Reveal Answer"
    **Correct Answer: 1,2,3**

    1.	Step 1: Create a Git source code repository. 2.	Step 2: Create a pipeline in AWS CodePipeline. Build and test containers in AWS CodeBuild. 3.	Step 3: Invoke Amazon SageMaker Pipelines to run all steps required for model training and deployment. 11

---

## Question 12

A company has significantly increased the amount of data that is stored as .csv files in an Amazon S3 bucket. Data transformation scripts and queries are now taking much longer than they used to take. An ML engineer must implement a solution to optimize the data for query performance. Which solution will meet this requirement with the LEAST operational overhead?

- **A.** Configure an AWS Lambda function to split the .csv files into smaller objects in the S3 bucket.
- **B.** Configure an AWS Glue job to drop columns that have string type values and to save the results to the S3 bucket.
- **C.** Configure an AWS Glue extract, transform, and load (ETL) job to convert the .csv files to Apache Parquet format.
- **D.** Configure an Amazon EMR cluster to process the data that is in the S3 bucket.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Configure an AWS Glue extract, transform, and load (ETL) job to convert the .csv files to Apache Parquet format. 12

---

## Question 13

An ML engineer is using a training job to fine-tune a deep learning model in Amazon SageMaker Studio. The ML engineer previously trained the same pre-trained model with a similar dataset. The ML engineer expects vanishing gradient, underutilized GPU, and overfitting problems. The ML engineer needs to implement a solution to detect these issues and to react in predefined ways when the issues occur. The solution also must provide comprehensive real-time metrics during the training. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use TensorBoard to monitor the training job. Publish the findings to an Amazon Simple Notification Service (Amazon SNS) topic. Create an AWS Lambda function to consume the findings and to initiate the predefined actions.
- **B.** Use Amazon CloudWatch default metrics to gain insights about the training job. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- **C.** Expand the metrics in Amazon CloudWatch to include the gradients in each training step. Use the metrics to invoke an AWS Lambda function to initiate the predefined actions.
- **D.** Use SageMaker Debugger built-in rules to monitor the training job. Configure the rules to initiate the predefined actions.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Use SageMaker Debugger built-in rules to monitor the training job. Configure the rules to initiate the predefined actions. 13

---

## Question 14

A company is using an Amazon Redshift database as its single data source. Some of the data is sensitive. A data scientist needs to use some of the sensitive data from the database. An ML engineer must give the data scientist access to the data without transforming the source data and without storing anonymized data in the database. Which solution will meet these requirements with the LEAST implementation effort?

- **A.** Configure dynamic data masking policies to control how sensitive data is shared with the data scientist at query time.
- **B.** Create a materialized view with masking logic on top of the database. Grant the necessary read permissions to the data scientist.
- **C.** Unload the Amazon Redshift data to Amazon S3. Use Amazon Athena to create schema-on-read with masking logic. Share the view with the data scientist.
- **D.** Unload the Amazon Redshift data to Amazon S3. Create an AWS Glue job to anonymize the data. Share the dataset with the data scientist.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Configure dynamic data masking policies to control how sensitive data is shared with the data scientist at query time. 14

---

## Question 15

A company uses Amazon Athena to query a dataset in Amazon S3. The dataset has a target variable that the company wants to predict. The company needs to use the dataset in a solution to determine if a model can predict the target variable. Which solution will provide this information with the LEAST development effort?

- **A.** Create a new model by using Amazon SageMaker Autopilot. Report the model's achieved performance.
- **B.** Implement custom scripts to perform data pre-processing, multiple linear regression, and performance evaluation. Run the scripts on Amazon EC2 instances.
- **C.** Configure Amazon Macie to analyze the dataset and to create a model. Report the model's achieved performance.
- **D.** Select a model from Amazon Bedrock. Tune the model with the data. Report the model's achieved performance.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Create a new model by using Amazon SageMaker Autopilot. Report the model's achieved performance. 15

---

## Question 16

A company deployed an Amazon SageMaker AI ML model to an endpoint by calling the CreateModel API operation. The network that was established with the API call includes two private subnets and one security group. The model must download data from an Amazon S3 bucket and must upload data to the S3 bucket. The traffic to the S3 bucket must not travel across the internet. Which solution will meet these requirements?

- **A.** Create a NAT gateway. Configure the security group to allow outbound connections. Configure route tables to redirect any traffic to the S3 bucket through the NAT gateway.
- **B.** Create a gateway VPC endpoint. Configure an endpoint policy that restricts access to the S3 bucket. Configure route tables to redirect any traffic to the S3 bucket through the endpoint.
- **C.** Create an interface VPC endpoint. Verify that the security group allows only outbound connections. Configure route tables to redirect any traffic to the S3 bucket through the endpoint.
- **D.** Create a Gateway Load Balancer VPC endpoint. Configure an IAM policy that restricts access to the S3 bucket. Configure route tables to redirect any traffic to the S3 bucket through the endpoint.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Create a gateway VPC endpoint. Configure an endpoint policy that restricts access to the S3 bucket. Configure route tables to redirect any traffic to the S3 bucket through the endpoint. 16

---

## Question 17

An ML engineer has an Amazon Comprehend custom model in Account A in the us-east-1 Region. The ML engineer needs to copy the model to Account B in the same Region. Which solution will meet this requirement with the LEAST development effort?

- **A.** Use Amazon S3 to make a copy of the model. Transfer the copy to Account B.
- **B.** Create a resource-based IAM policy. Use the Amazon Comprehend ImportModel API operation to copy the model to Account B.
- **C.** Use AWS DataSync to replicate the model from Account A to Account B.
- **D.** Create an AWS Site-to-Site VPN connection between Account A and Account B to transfer the model.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Create a resource-based IAM policy. Use the Amazon Comprehend ImportModel API operation to copy the model to Account B. 17

---

## Question 18

A company is building an enterprise AI platform. The company must catalog models for production, manage model versions, and associate metadata such as training metrics with models. The company needs to eliminate the burden of managing different versions of models. Which solution will meet these requirements?

- **A.** Use the Amazon SageMaker Model Registry to catalog the models. Create unique tags for each model version. Create key-value pairs to maintain associated metadata.
- **B.** Use the Amazon SageMaker Model Registry to catalog the models. Create model groups for each model to manage the model versions and to maintain associated metadata.
- **C.** Create a separate Amazon Elastic Container Registry (Amazon ECR) repository for each model. Use the repositories to catalog the models and to manage model versions and associated metadata.
- **D.** Create a separate Amazon Elastic Container Registry (Amazon ECR) repository for each model. Create unique tags for each model version. Create key-value pairs to maintain associated metadata.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use the Amazon SageMaker Model Registry to catalog the models. Create model groups for each model to manage the model versions and to maintain associated metadata. 18

---

## Question 19

An ML engineer needs to run intensive model training jobs each month that can take 48 to 72 hours to run. The training jobs can be interrupted and resumed without major issues. The ML engineer has a fixed budget and needs to optimize computing resources. Which solution will meet these requirements MOST cost-effectively?

- **A.** Purchase Reserved Instances with a partial upfront payment.
- **B.** Purchase On-Demand Instances with no commitment.
- **C.** Purchase Amazon SageMaker AI Savings Plans.
- **D.** Purchase Spot Instances that use automated checkpoints.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Purchase Spot Instances that use automated checkpoints. 19

---

## Question 20

A company is running ML models on premises by using custom Python scripts and proprietary datasets. The company is using PyTorch. The model building requires unique domain knowledge. The company needs to move the models to AWS. Which solution will meet these requirements with the LEAST development effort?

- **A.** Use SageMaker AI built-in algorithms to train the proprietary datasets.
- **B.** Use SageMaker AI script mode and premade images for ML frameworks.
- **C.** Build a container on AWS that includes custom packages and a choice of ML frameworks.
- **D.** Purchase similar production models through AWS Marketplace.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use SageMaker AI script mode and premade images for ML frameworks. 20

---

## Question 21

A company has a conversational AI assistant that sends requests through Amazon Bedrock to an Anthropic Claude large language model (LLM). Users report that when they ask similar questions multiple times, they sometimes receive different answers. An ML engineer needs to improve the responses to be more consistent and less random. Which solution will meet these requirements?

- **A.** Increase the temperature parameter and the top k parameter.
- **B.** Increase the temperature parameter. Decrease the top k parameter.
- **C.** Decrease the temperature parameter. Increase the top k parameter.
- **D.** Decrease the temperature parameter and the top k parameter.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Decrease the temperature parameter and the top k parameter. 21

---

## Question 22

An ML engineer is evaluating several ML models and must choose one model to use in production. The cost of false negative predictions by the models is much higher than the cost of false positive predictions. Which metric finding should the ML engineer prioritize the MOST when choosing the model?

- **A.** Low precision
- **B.** High precision
- **C.** Low recall
- **D.** High recall

??? success "Reveal Answer"
    **Correct Answer: D**

    D. High recall 22

---

## Question 23

A company uses an Amazon SageMaker AI ML model to make real-time inferences. The company has configured auto scaling for the Amazon EC2 instances that SageMaker AI uses for the inferences. During times of peak usage, new instances launch before existing instances are fully ready. As a result, the model experiences inefficiencies and delays. Which solution will optimize the scaling process without affecting response times?

- **A.** Change to a multi-model endpoint configuration in SageMaker AI.
- **B.** Integrate Amazon API Gateway and AWS Lambda to manage invocations of the SageMaker AI inference endpoint.
- **C.** Decrease the cooldown period for scale-in activities. Increase the maximum number of instances.
- **D.** Increase the cooldown period after scale-out activities.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Decrease the cooldown period for scale-in activities. Increase the maximum number of instances. 23

---

## Question 24

A company is planning to use Amazon SageMaker AI to make classification ratings that are based on images. The company has 6 TB of training data that is stored on an Amazon FSx for NetApp ONTAP system virtual machine (SVM). The SVM is in the same VPC as SageMaker AI. An ML engineer must make the training data accessible for ML models that are in the SageMaker AI environment. Which solution will meet these requirements?

- **A.** Mount the FSx for ONTAP file system as a volume to the SageMaker AI instance.
- **B.** Create an Amazon S3 bucket. Use Mountpoint for Amazon S3 to link the S3 bucket to the FSx for ONTAP file system.
- **C.** Create a catalog connection from SageMaker Data Wrangler to the FSx for ONTAP file system.
- **D.** Create a direct connection from SageMaker Data Wrangler to the FSx for ONTAP file system.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Mount the FSx for ONTAP file system as a volume to the SageMaker AI instance. 24

---

## Question 25

A company is using Amazon SageMaker AI to deploy a new recommendation model for its e-commerce website. The model must use data from all client website interactions as input. Traffic is variable throughout the day. The company needs to create an inference endpoint for the model. Which type of inference endpoint will meet these requirements MOST cost-effectively?

- **A.** Batch transform inference endpoint
- **B.** Asynchronous inference endpoint
- **C.** Real-time inference endpoint
- **D.** Serverless inference endpoint

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Serverless inference endpoint 25

---

## Question 26

A logistics company has installed in-vehicle cameras for basic monitoring of its drivers. The company wants to improve driver safety by identifying distractions that could lead to accidents. Which solution will meet this requirement with the LEAST operational effort?

- **A.** Use Amazon Rekognition eye gaze direction detection to monitor driver behavior and identify distractions.
- **B.** Use Amazon SageMaker AI to customize an AI model to monitor driver behavior and identify distractions.
- **C.** Integrate a third-party driver monitoring system with Amazon Rekognition to monitor driver behavior and identify distractions.
- **D.** Use Amazon Comprehend to analyze text-based driver feedback and identify distractions.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use Amazon Rekognition eye gaze direction detection to monitor driver behavior and identify distractions. 26

---

## Question 27

A music streaming company constantly streams song ratings from an application to an Amazon S3 bucket. The company wants to use the ratings as an input for training and inference of an Amazon SageMaker AI model. The company has an AWS Glue Data Catalog that is configured with the S3 bucket as the source. An ML engineer needs to implement a solution to create a repository for this data. The solution must ensure that the data stays synchronized during batch training and real-time inference. Which solution will meet these requirements?

- **A.** Ingest data into SageMaker Feature Store from the S3 bucket. Apply tags and indexes.
- **B.** Use Amazon Athena. Create tables by using CREATE TABLE AS SELECT (CTAS) queries to group data.
- **C.** Use AWS Lake Formation. Apply tag-based control on the data.
- **D.** Use the Generate Data Insights function in SageMaker Data Wrangler.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Ingest data into SageMaker Feature Store from the S3 bucket. Apply tags and indexes. 27

---

## Question 28

A company has implemented a data ingestion pipeline for sales transactions from its e-commerce website. The company uses Amazon Data Firehose to ingest data into Amazon OpenSearch Service. The buffer interval of the Firehose stream is set for 60 seconds. An OpenSearch linear model generates real-time sales forecasts based on the data and presents the data in an OpenSearch dashboard. The company needs to optimize the data ingestion pipeline to support sub-second latency for the real-time dashboard. Which change to the architecture will meet these requirements?

- **A.** Use zero buffering in the Firehose stream. Tune the batch size that is used in the PutRecordBatch operation.
- **B.** Replace the Firehose stream with an AWS DataSync task. Configure the task with enhanced fan-out consumers.
- **C.** Increase the buffer interval of the Firehose stream from 60 seconds to 120 seconds.
- **D.** Replace the Firehose stream with an Amazon Simple Queue Service (Amazon SQS) queue.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use zero buffering in the Firehose stream. Tune the batch size that is used in the PutRecordBatch operation. 28

---

## Question 29

A company is creating an ML model to identify defects in a product. The company has gathered a dataset and has stored the dataset in TIFF format in Amazon S3. The dataset contains 200 images in which the most common defects are visible. The dataset also contains 1,800 images in which there is no defect visible. An ML engineer trains the model and notices poor performance in some classes. The ML engineer identifies a class imbalance problem in the dataset. What should the ML engineer do to solve this problem?

- **A.** Use a few hundred images and Amazon Rekognition Custom Labels to train a new model.
- **B.** Undersample the 200 images in which the most common defects are visible.
- **C.** Oversample the 200 images in which the most common defects are visible.
- **D.** Use all 2,000 images and Amazon Rekognition Custom Labels to train a new model.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Oversample the 200 images in which the most common defects are visible. 29

---

## Question 30

A company has an ML model in Amazon SageMaker AI. An ML engineer needs to implement a monitoring solution to automatically detect changes in the input data distribution of model features. Which solution will meet this requirement with the LEAST operational overhead?

- **A.** Configure SageMaker Model Monitor. Establish a data quality baseline. Ensure that the emit metrics option is enabled in the baseline constraints file. Configure an Amazon CloudWatch alarm to notify the company about changes in specific metrics that are related to data quality.
- **B.** Configure SageMaker Model Monitor. Establish a model quality baseline. Ensure that the comparison_method option is set to Robust in the baseline constraints file. Configure an Amazon CloudWatch alarm to notify the company about changes in model quality metrics.
- **C.** Use SageMaker Debugger with custom rules to track shifts in feature distributions. Configure Amazon CloudWatch alarms to notify the company when the rules detect significant changes.
- **D.** Use Amazon CloudWatch to directly observe the SageMaker AI endpoint's performance metrics. Manually analyze the CloudWatch logs for indicators of data drift or shifts in feature distribution.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Configure SageMaker Model Monitor. Establish a data quality baseline. Ensure that the emit metrics option is enabled in the baseline constraints file. Configure an Amazon CloudWatch alarm to notify the company about changes in specific metrics that are related to data quality. 30

---

## Question 31

A company runs an Amazon SageMaker AI domain in a public subnet of a newly created VPC. The network is configured properly, and ML engineers can access the SageMaker AI domain. Recently, the company discovered suspicious traffic to the domain from a specific IP address. The company needs to block traffic from the specific IP address. Which update to the network configuration will meet this requirement?

- **A.** Create a security group inbound rule to deny traffic from the specific IP address. Assign the security group to the domain.
- **B.** Create a network ACL inbound rule to deny traffic from the specific IP address. Assign the rule to the default network ACL for the subnet where the domain is located.
- **C.** Create a shadow variant for the domain. Configure SageMaker Inference Recommender to send traffic from the specific IP address to the shadow endpoint.
- **D.** Create a VPC route table to deny inbound traffic from the specific IP address. Assign the route table to the domain.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Create a network ACL inbound rule to deny traffic from the specific IP address. Assign the rule to the default network ACL for the subnet where the domain is located. 31

---

## Question 32

!!! warning "Select 2"

An ML engineer is training a simple neural network model. The ML engineer tracks the performance of the model over time on a validation dataset. The model's performance improves substantially at first and then degrades after a specific number of epochs. Which solutions will mitigate this problem? (Select TWO)

- **A.** Enable early stopping on the model.
- **B.** Increase dropout in the layers.
- **C.** Increase the number of layers.
- **D.** Increase the number of neurons.
- **E.** Investigate and reduce the sources of model bias.

??? success "Reveal Answer"
    **Correct Answer: A,B**

    A. Enable early stopping on the model. AND B. Increase dropout in the layers. 32

---

## Question 33

A company has a Retrieval Augmented Generation (RAG) application that uses a vector database to store embeddings of documents. The company must migrate the application to AWS and must implement a solution that provides semantic search of text files. The company has already migrated the text repository to an Amazon S3 bucket. Which solution will meet these requirements?

- **A.** Use an AWS Batch job to process the files and generate embeddings. Use AWS Glue to store the embeddings. Use SQL queries to perform the semantic searches.
- **B.** Use a custom Amazon SageMaker AI notebook to run a custom script to generate embeddings. Use SageMaker Feature Store to store the embeddings. Use SQL queries to perform the semantic searches.
- **C.** Use the Amazon Kendra S3 connector to ingest the documents from the S3 bucket into Amazon Kendra. Query Amazon Kendra to perform the semantic searches.
- **D.** Use an Amazon Textract asynchronous job to ingest the documents from the S3 bucket. Query Amazon Textract to perform the semantic searches.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Use the Amazon Kendra S3 connector to ingest the documents from the S3 bucket into Amazon Kendra. Query Amazon Kendra to perform the semantic searches. 33

---

## Question 34

A company is building an Amazon SageMaker AI pipeline for an ML model. The pipeline uses distributed processing and training. An ML engineer needs to encrypt network communication between instances that run distributed jobs. The ML engineer configures the distributed jobs to run in a private VPC. What should the ML engineer do to meet the encryption requirement?

- **A.** Enable network isolation.
- **B.** Configure traffic encryption by using security groups.
- **C.** Enable inter-container traffic encryption.
- **D.** Enable VPC flow logs.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Enable inter-container traffic encryption. 34

---

## Question 35

A company has trained an ML model that is packaged in a container. The company will integrate the model with an existing Python web application. The company needs to host the model on AWS by using Kubernetes. The company does not want to manage the control plane and must provision the resources in a repeatable manner. The infrastructure must be provisioned by using Python. Which solution will meet these requirements?

- **A.** Use AWS CloudFormation to provision Amazon EC2 instances in multiple Availability Zones. Set up a Kubernetes cluster. Host the model container on the Kubernetes cluster.
- **B.** Use the AWS CLI to provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Store the image in an Amazon Elastic Container Registry (Amazon ECR) repository. Host the model container on the EKS cluster.
- **C.** Use the AWS Cloud Development Kit (AWS CDK) to provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Store the image in an Amazon Elastic Container Registry (Amazon ECR) repository. Host the model container on the EKS cluster.
- **D.** Use AWS CloudFormation to provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Store the image in an Amazon Elastic Container Registry (Amazon ECR) repository. Host the model container on the EKS cluster.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Use the AWS Cloud Development Kit (AWS CDK) to provision an Amazon Elastic Kubernetes Service (Amazon EKS) cluster. Store the image in an Amazon Elastic Container Registry (Amazon ECR) repository. Host the model container on the EKS cluster. 35

---

## Question 36

A utility company is using a deep learning model in an Amazon SageMaker AI notebook to predict energy demand. During the hyperparameter selection process of model training, the company is concerned that the learning rate might be too high for the model to converge. The company needs to assess the learning rate during model training. Which solution will meet this requirement?

- **A.** Configure the training job to use a SageMaker Debugger hook. Monitor the built- in confusion rule.
- **B.** Configure the training job to use a SageMaker Debugger hook. Monitor the built- in WeightUpdateRatio rule.
- **C.** Configure the training job to use SageMaker Clarify to monitor feature attributions that are based on Shapley Additive explanations (SHAP) values.
- **D.** Configure the training job to use SageMaker Clarify to monitor feature attributions that are based on asymmetric Shapley values.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Configure the training job to use a SageMaker Debugger hook. Monitor the built-in WeightUpdateRatio rule. 36

---

## Question 37

An ML engineer trained an ML model on Amazon SageMaker AI to detect automobile accidents from closed-circuit TV footage. The ML engineer used SageMaker Data Wrangler to create a training dataset of images of accidents and non-accidents. The model performed well during training and validation. However, the model is underperforming in production because of variations in the quality of the images from various cameras. Which solution will improve the model's accuracy in the LEAST amount of time?

- **A.** Collect more images from all the cameras. Use Data Wrangler to prepare a new training dataset.
- **B.** Recreate the training dataset by using the Data Wrangler corrupt image transform. Specify the impulse noise option.
- **C.** Recreate the training dataset by using the Data Wrangler enhance image contrast transform. Specify the Gamma contrast option.
- **D.** Recreate the training dataset by using the Data Wrangler resize image transform. Crop all images to the same size.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Recreate the training dataset by using the Data Wrangler resize image transform. Crop all images to the same size. 37

---

## Question 38

An ML engineer is building a generative AI application on Amazon Bedrock by using large language models (LLMs). Select the correct generative AI term from the list for each description. 1.	Text representation of basic units of data processed by LLMs 2.	High-dimensional vectors that contain the semantic meaning of text 3.	Enrichment of information from additional data sources to improve a generated response


??? success "Reveal Answer"
    **Correct Answer: ?**

    1.	Text representation of basic units of data processed by LLMs: Token 38 2.	High-dimensional vectors that contain the semantic meaning of text: Embedding 39 3.	Enrichment of information from additional data sources to improve a generated response: Retrieval Augmented Generation (RAG) 40

---

## Question 39

!!! warning "Select 2"

An ML engineer has developed a binary classification model outside of Amazon SageMaker AI. The ML engineer needs to make the model accessible to a SageMaker Canvas user for additional tuning. The model artifacts are stored in an Amazon S3 bucket. The ML engineer and the Canvas user are part of the same SageMaker AI domain. Which combination of requirements must be met so that the ML engineer can share the model with the Canvas user? (Select TWO)

- **A.** The ML engineer and the Canvas user must be in separate SageMaker AI domains.
- **B.** The Canvas user must have permissions to access the S3 bucket where the model artifacts are stored.
- **C.** The model must be registered in the SageMaker Model Registry.
- **D.** The ML engineer must host the model on AWS Marketplace.
- **E.** The ML engineer must deploy the model to a SageMaker AI endpoint.

??? success "Reveal Answer"
    **Correct Answer: B,C**

    B. The Canvas user must have permissions to access the S3 bucket where the model artifacts are stored. AND C. The model must be registered in the SageMaker Model Registry. 41

---

## Question 40

An ML engineer is deploying a generative AI model-based customer support agent that uses Amazon SageMaker AI for inference. The customer support agent must respond to customer questions about topics such as shipping policies, refund processes, and account management. The generative AI model generates one token at a time. Customers report dissatisfaction with how long the customer support agent takes to generate lengthy responses to questions. The ML engineer must apply an inference optimization technique to improve the performance of the customer support agent. Which solution will meet this requirement?

- **A.** Compilation
- **B.** Speculative decoding
- **C.** Quantization
- **D.** Fast model loading

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Speculative decoding 42

---

## Question 41

A company has developed a computer vision model. The company needs to deploy the model into production on Amazon SageMaker AI. The company has not hosted a model on SageMaker AI previously. An ML engineer needs to implement a solution to track model versions. The solution also must provide recommendations about which Amazon EC2 instance types to use to host the model. Which solution will meet these requirements?

- **A.** Register the model in Amazon Elastic Container Registry (Amazon ECR). Use AWS Compute Optimizer for recommendations about instance types.
- **B.** Register the model in the SageMaker Model Registry. Use SageMaker Autopilot for recommendations about instance types.
- **C.** Register the model in the SageMaker Model Registry. Use SageMaker Inference Recommender for recommendations about instance types.
- **D.** Register the model in Amazon Elastic Container Registry (Amazon ECR). Use SageMaker Experiments for recommendations about instance types.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Register the model in the SageMaker Model Registry. Use SageMaker Inference Recommender for recommendations about instance types. 43

---

## Question 42

A financial company receives a high volume of real-time market data streams from an external provider. The streams consist of thousands of JSON records every second. The company needs to implement a scalable solution on AWS to identify anomalous data points. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Ingest real-time data into Amazon Kinesis data streams. Use the built-in RANDOM_CUT_FOREST function in Amazon Managed Service for Apache Flink to process the data streams and to detect data anomalies.
- **B.** Ingest real-time data into Amazon Kinesis data streams. Deploy an Amazon SageMaker AI endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- **C.** Ingest real-time data into Apache Kafka on Amazon EC2 instances. Deploy an Amazon SageMaker AI endpoint for real-time outlier detection. Create an AWS Lambda function to detect anomalies. Use the data streams to invoke the Lambda function.
- **D.** Send real-time data to an Amazon Simple Queue Service (Amazon SQS) FIFO queue. Create an AWS Lambda function to consume the queue messages. Program the Lambda function to start an AWS Glue extract, transform, and load (ETL) job for batch processing and anomaly detection.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Ingest real-time data into Amazon Kinesis data streams. Use the built-in RANDOM_CUT_FOREST function in Amazon Managed Service for Apache Flink to process the data streams and to detect data anomalies. 44

---

## Question 43

A company needs to ingest data from data sources into Amazon SageMaker Data Wrangler. The data sources are Amazon S3, Amazon Redshift, and Snowflake. The ingested data must always be up to date with the latest changes in the source systems. Which solution will meet these requirements?

- **A.** Use direct connections to import data from the data sources into Data Wrangler.
- **B.** Use cataloged connections to import data from the data sources into Data Wrangler.
- **C.** Use AWS Glue to extract data from the data sources. Use AWS Glue also to import the data directly into Data Wrangler.
- **D.** Use AWS Lambda to extract data from the data sources. Use Lambda also to import the data directly into Data Wrangler.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use direct connections to import data from the data sources into Data Wrangler. 45

---

## Question 44

A company is developing a generative AI conversational interface to assist customers with payments. The company wants to use an ML solution to detect customer intent. The company does not have training data to train a model. Which solution will meet these requirements?

- **A.** Fine-tune a sequence-to-sequence (seq2seq) algorithm in Amazon SageMaker JumpStart.
- **B.** Use an LLM from Amazon Bedrock with zero-shot learning.
- **C.** Use the Amazon Comprehend DetectEntities API.
- **D.** Run an LLM from Amazon Bedrock on Amazon EC2 instances.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use an LLM from Amazon Bedrock with zero-shot learning. 46

---

## Question 45

A company uses a hybrid cloud environment. A model that is deployed on premises uses data in Amazon S3 to provide customers with a live conversational engine. The model is using sensitive data. An ML engineer needs to implement a solution to identify and remove the sensitive data. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Deploy the model on Amazon SageMaker AI. Create a set of AWS Lambda functions to identify and remove the sensitive data.
- **B.** Deploy the model on an Amazon Elastic Container Service (Amazon ECS) cluster that uses AWS Fargate. Create an AWS Batch job to identify and remove the sensitive data.
- **C.** Use Amazon Macie to identify the sensitive data. Create a set of AWS Lambda functions to remove the sensitive data.
- **D.** Use Amazon Comprehend to identify the sensitive data. Launch Amazon EC2 instances to remove the sensitive data.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Use Amazon Macie to identify the sensitive data. Create a set of AWS Lambda functions to remove the sensitive data. 47

---

## Question 46

An ML engineer needs to use an Amazon EMR cluster to process large volumes of data in batches. Any data loss is unacceptable. Which instance purchasing option will meet these requirements MOST cost-effectively?

- **A.** Run the primary node, core nodes, and task nodes on On-Demand Instances.
- **B.** Run the primary node, core nodes, and task nodes on Spot Instances.
- **C.** Run the primary node on an On-Demand Instance. Run the core nodes and task nodes on Spot Instances.
- **D.** Run the primary node and core nodes on On-Demand Instances. Run the task nodes on Spot Instances.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Run the primary node and core nodes on On-Demand Instances. Run the task nodes on Spot Instances. 48

---

## Question 47

An ML engineer normalized training data by using min-max normalization in AWS Glue DataBrew. The ML engineer must normalize the production inference data in the same way as the training data before passing the production inference data to the model for predictions. Which solution will meet this requirement?

- **A.** Apply statistics from a well-known dataset to normalize the production samples.
- **B.** Keep the min-max normalization statistics from the training set. Use these values to normalize the production samples.
- **C.** Calculate a new set of min-max normalization statistics from a batch of production samples. Use these values to normalize all the production samples.
- **D.** Calculate a new set of min-max normalization statistics from each production sample. Use these values to normalize all the production samples.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Keep the min-max normalization statistics from the training set. Use these values to normalize the production samples. 49

---

## Question 48

A company collects customer data every day. The company stores the data as compressed files in an Amazon S3 bucket that is partitioned by date. Every month, analysts download the data, process the data to check the data quality, and then upload the data to Amazon QuickSight dashboards. An ML engineer needs to implement a solution to automatically check the data quality before the data is sent to QuickSight. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Run an AWS Glue crawler every month to update the AWS Glue Data Catalog. Use AWS Glue Data Quality rules to check the data quality.
- **B.** Use an AWS Glue trigger to run an AWS Glue crawler every month to update the AWS Glue Data Catalog. Create an AWS Glue job that loads the data into a PySpark DataFrame. Configure the job to apply custom functions and to evaluate the data quality.
- **C.** Run Python scripts on an AWS Lambda function every month to evaluate data quality. Configure the S3 bucket to invoke the Lambda function when objects are added to the S3 bucket.
- **D.** Configure the S3 bucket to send event notifications to an Amazon Simple Queue Service (Amazon SQS) queue when objects are uploaded. Use Amazon CloudWatch insights every month for the SQS queue to evaluate the data quality.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Run an AWS Glue crawler every month to update the AWS Glue Data Catalog. Use AWS Glue Data Quality rules to check the data quality. 50

---

## Question 49

A company is building a deep learning model on Amazon SageMaker AI. The company uses a large amount of data as the training dataset. The company needs to optimize the model's hyperparameters to minimize the loss function on the validation dataset. Which hyperparameter tuning strategy will accomplish this goal with the LEAST computation time?

- **A.** Hyperband
- **B.** Grid search
- **C.** Bayesian optimization
- **D.** Random search

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Hyperband 51

---

## Question 50

A company is using Amazon SageMaker to deploy a new version of its ML model. Select the correct SageMaker traffic shifting strategy from the following list for each use case. 1.	Shift traffic in two steps to validate the new model version 2.	Shift traffic to the new model version in the shortest amount of time 3.	Incrementally shift traffic to the new model version over time


??? success "Reveal Answer"
    **Correct Answer: ?**

    1.	Shift traffic in two steps to validate the new model version: Canary traffic shifting 52 2.	Shift traffic to the new model version in the shortest amount of time: All at once traffic shifting 53 3.	Incrementally shift traffic to the new model version over time: Linear traffic shifting 54

---

## Question 51

!!! warning "Select 2"

An ML engineer is designing an AI-powered traffic management system to adjust traffic lights during predicted congestion. The system must use near real-time inference to generate predictions to help prevent traffic collisions. The system must use a batch processing pipeline to perform historical analysis of the predictions to continuously refine and improve the model. The historical analysis will take several hours to evaluate how well the predictions correlate with actual outcomes. The system must be able to scale inference endpoints appropriately to meet demand. Which combination of solutions will meet these requirements? (Select TWO)

- **A.** Use Amazon SageMaker real-time inference endpoints. Configure the endpoints to scale automatically based on a target tracking scaling policy that uses the metric ConcurrentInvocationsPerInstance.
- **B.** Configure reserved concurrency for AWS Lambda functions to process streaming data. Use Lambda SnapStart to connect the Lambda functions to Amazon SageMaker real-time endpoints to support near real-time traffic predictions.
- **C.** Configure an Amazon SageMaker Processing job for batch analysis of historical prediction data. Use Amazon EventBridge to schedule the job to run daily. Allow several hours for in-depth analysis to refine and improve the traffic management model.
- **D.** Use an Amazon EC2 Auto Scaling group to host containers to support the batch analysis of historical prediction data. Configure scaling based on Amazon CloudWatch metrics to analyze historical traffic patterns and model performance over multiple hours.
- **E.** Use an AWS Lambda function to perform the historical analysis. Use Amazon EventBridge to invoke the Lambda function.

??? success "Reveal Answer"
    **Correct Answer: A,C**

    A. Use Amazon SageMaker real-time inference endpoints. Configure the endpoints to scale automatically based on a target tracking scaling policy that uses the metric ConcurrentInvocationsPerInstance. AND C. Configure an Amazon SageMaker Processing job for batch analysis of historical prediction data. Use Amazon EventBridge to schedule the job to run daily. 55

---

## Question 52

A company needs to analyze a large dataset that is stored in Amazon S3 in Apache Parquet format. The company wants to use one-hot encoding for some of the columns. The company needs a no-code solution to transform the data. The solution must store the transformed data back to the same S3 bucket for model training. Which solution will meet these requirements?

- **A.** Configure an AWS Glue DataBrew project that connects to the data. Use the DataBrew interactive interface to create a recipe that performs the one-hot encoding transformation. Create a job to apply the transformation and to write the output back to an S3 bucket.
- **B.** Configure an AWS Glue Data Catalog table that points to the data. Use Amazon Athena to write SQL commands to perform the one-hot encoding transformation. Configure Athena to write the query results back to an S3 bucket.
- **C.** Configure an AWS Glue Data Catalog table that points to the data. Create an AWS Glue ETL interactive notebook. Use the notebook to perform the one-hot encoding transformation. Run the configured cells and write the results back to an S3 bucket.
- **D.** Configure an Amazon Redshift cluster to access the data by using Redshift Spectrum. Use SQL commands to perform the one-hot encoding transformation within Amazon Redshift. Configure Amazon Redshift to write the results back to an S3 bucket.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Configure an AWS Glue DataBrew project that connects to the data. Use the DataBrew interactive interface to create a recipe that performs the one-hot encoding transformation. Create a job to apply the transformation and to write the output back to an S3 bucket. 56

---

## Question 53

A company is using an ML model to classify motion in videos. The data is stored in MP4 format in Amazon S3. When the company created the model, the company needed 4 months to label all the video frames. The company needs to retrain the model with an existing training workflow in Amazon SageMaker AI. An ML engineer must implement a solution that decreases the labeling time. Which solution will meet these requirements?

- **A.** Use SageMaker Ground Truth to annotate the video frames.
- **B.** Use SageMaker JumpStart to use pre-trained computer vision models to develop a labeling model.
- **C.** Use SageMaker Data Wrangler to create a data workflow. Use the workflow to optimize the labeling process.
- **D.** Use the labeling interface of Amazon Augmented AI (Amazon A2I) with Amazon Rekognition to label the video frames.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use SageMaker JumpStart to use pre-trained computer vision models to develop a labeling model. 57

---

## Question 54

A company uses Amazon SageMaker AI to support ML workflows such as model training and deployment. Select the correct registry from the following list to meet the requirements for each use case with the LEAST operational overhead. Each registry should be selected one or more times. (Options: Amazon Elastic Container Registry (ECR), SageMaker Model Registry) 1.	Tag model packages and use model package groups that include container images for training and deployment. 2.	Store predefined language packages, kernels, and relevant dependencies. 3.	Organize models and their images into model groups for better discoverability. 4.	Pull built-in SageMaker AI images for model training.


??? success "Reveal Answer"
    **Correct Answer: ?**

    1.	Tag model packages... -> SageMaker Model Registry 58 2.	Store predefined language packages... -> Amazon Elastic Container Registry (Amazon ECR) 59 3.	Organize models... -> SageMaker Model Registry 60 4.	Pull built-in SageMaker AI images... -> Amazon Elastic Container Registry (Amazon ECR) 61

---

## Question 55

A company regularly receives new training data from the vendor of an ML model. The vendor delivers cleaned and prepared data to the company's Amazon S3 bucket every 3-4 days. The company has an Amazon SageMaker AI pipeline to retrain the model. An ML engineer needs to implement a solution to run the pipeline when new data is uploaded to the S3 bucket. Which solution will meet these requirements with the LEAST operational effort?

- **A.** Create an S3 Lifecycle rule to transfer the data to the SageMaker AI training instance and to initiate training.
- **B.** Create an AWS Lambda function that scans the S3 bucket. Program the Lambda function to initiate the pipeline when new data is uploaded.
- **C.** Create an Amazon EventBridge rule that has an event pattern that matches the S3 upload. Configure the pipeline as the target of the rule.
- **D.** Use Amazon Managed Workflows for Apache Airflow (Amazon MWAA) to orchestrate the pipeline when new data is uploaded.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Create an Amazon EventBridge rule that has an event pattern that matches the S3 upload. Configure the pipeline as the target of the rule. 62

---

## Question 56

A company is training a new ML model to replace a model that is deployed on an Amazon SageMaker AI real-time endpoint. An ML engineer needs to determine the latency and the accuracy of the new model. The ML engineer must evaluate the new model in a production scenario without affecting the users of the existing model. Which solution will meet these requirements?

- **A.** Perform a blue/green deployment with linear traffic shifting.
- **B.** Perform a blue/green deployment with canary traffic shifting.
- **C.** Perform a rolling deployment with a rolling batch size of 50% of the current fleet.
- **D.** Perform shadow testing with a traffic sampling percentage of 100%.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Perform shadow testing with a traffic sampling percentage of 100%. 63

---

## Question 57

A customer call center uses Amazon Transcribe to convert hundreds of audio recordings of conversations between customers and support agents to text files. The call center wants to use the text files to train an ML model. To comply with industry regulations, the call center must remove customer names, addresses, and phone numbers from the training text files. Which solution will meet these requirements with the LEAST development effort?

- **A.** Use Amazon Bedrock Guardrails to process and redact personal information from the text files.
- **B.** Use the AWS Glue Detect PII transform to remove personal information from the text files.
- **C.** Store the text files in Amazon S3 buckets. Use S3 Object Lambda functions to redact personal information.
- **D.** Configure an Amazon SageMaker Data Wrangler custom transformation to remove personal information from the text files.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Use the AWS Glue Detect PII transform to remove personal information from the text files. 64

---

## Question 58

An ML engineer is developing a linear regression ML model. The model shows high accuracy on the training dataset but performs poorly on unseen new data. Which action should the ML engineer take to address this issue?

- **A.** Increase the complexity of the model to capture more patterns in the training data.
- **B.** Apply ML techniques such as cross-validation and regularization. Use Amazon SageMaker Experiments to track and compare different model versions and their performance metrics.
- **C.** Use Amazon SageMaker Debugger to monitor for convergence issues. Directly deploy the model into production. Use Amazon SageMaker Clarify to interpret model outputs on new data. Adjust the model based on these insights.
- **D.** Increase the size of the training dataset without adjusting the size of the model. Retrain the model on the new data. Generate a confusion matrix to analyze the results.

??? success "Reveal Answer"
    **Correct Answer: B**

    B. Apply ML techniques such as cross-validation and regularization. Use Amazon SageMaker Experiments to track and compare different model versions and their performance metrics. 65

---

## Question 59

An ML engineer is training a text generation model on Amazon SageMaker AI. After several epochs, the loss function does not converge, and the model's accuracy on the validation dataset starts to show oscillating results. The ML engineer needs to ensure that the model achieves generalization. Which solution will meet this requirement?

- **A.** Increase the learning rate and decrease the mini-batch size.
- **B.** Increase the learning rate as the number of epochs increases.
- **C.** Decrease the learning rate and increase the mini-batch size.
- **D.** Decrease the learning rate and decrease the mini-batch size.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Decrease the learning rate and increase the mini-batch size. 66

---

## Question 60

An ML engineer needs to use an ML model to predict the price of apartments in a specific location. Which metric should the ML engineer use to evaluate the model's performance?

- **A.** Accuracy
- **B.** Area Under the ROC Curve (AUC)
- **C.** F1 score
- **D.** Mean absolute error (MAE)

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Mean absolute error (MAE) 67

---

## Question 61

An ML engineer is setting up an Amazon SageMaker AI pipeline for an ML model. The pipeline must automatically initiate a re-training job if any data drift is detected. How should the ML engineer set up the pipeline to meet this requirement?

- **A.** Use an AWS Glue crawler and an AWS Glue extract, transform, and load (ETL) job to detect data drift. Use AWS Glue triggers to automate the re-training job.
- **B.** Use Amazon Managed Service for Apache Flink to detect data drift. Use an AWS Lambda function to automate the re-training job.
- **C.** Use SageMaker Model Monitor to detect data drift. Use an AWS Lambda function to automate the re-training job.
- **D.** Use Amazon QuickSight anomaly detection to detect data drift. Use an AWS Step Functions workflow to automate the re-training job.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Use SageMaker Model Monitor to detect data drift. Use an AWS Lambda function to automate the re-training job. 68

---

## Question 62

An ML engineer needs to process thousands of existing CSV documents and new CSV documents that are uploaded. The CSV documents are stored in a central Amazon S3 bucket and have the same number of columns. One of the columns is a transaction date. The ML engineer must query the data based on the transaction date. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use an Amazon Athena CREATE TABLE AS SELECT (CTAS) statement to create a table based on the transaction date from data in the central S3 bucket. Query the objects from the table.
- **B.** Create a new S3 bucket for processed data. Set up S3 replication from the central S3 bucket to the new S3 bucket. Use S3 Object Lambda to query the objects based on transaction date.
- **C.** Create a new S3 bucket for processed data. Use AWS Glue for Apache Spark to create a job to query the CSV objects based on transaction date. Configure the job to store the results in the new S3 bucket.
- **D.** Create a new S3 bucket for processed data. Use Amazon Data Firehose to transfer the data from the central S3 bucket to the new S3 bucket. Configure Firehose to run an AWS Lambda function to query the data based on transaction date.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use an Amazon Athena CREATE TABLE AS SELECT (CTAS) statement to create a table based on the transaction date from data in the central S3 bucket. Query the objects from the table. 69

---

## Question 63

An ML engineer needs to use AWS services to identify and extract meaningful unique keywords from documents. Which solution will meet these requirements with the LEAST operational overhead?

- **A.** Use the Natural Language Toolkit (NLTK) library on Amazon EC2 instances for text pre-processing. Use the Latent Dirichlet Allocation (LDA) algorithm to identify and extract relevant keywords.
- **B.** Use Amazon SageMaker AI and the BlazingText algorithm. Apply custom pre- processing steps for stemming and removal of stop words. Calculate term frequency-inverse document frequency (TF-IDF) scores to identify and extract relevant keywords.
- **C.** Store the documents in an Amazon S3 bucket. Create AWS Lambda functions to process the documents and to run Python scripts for stemming and removal of stop words. Use bigram and trigram techniques to identify and extract relevant keywords.
- **D.** Use Amazon Comprehend custom entity recognition and key phrase extraction to identify and extract relevant keywords.

??? success "Reveal Answer"
    **Correct Answer: D**

    D. Use Amazon Comprehend custom entity recognition and key phrase extraction to identify and extract relevant keywords. 70

---

## Question 64

A company is using ML to predict the presence of a specific weed in a farmer's field. The company is using the Amazon SageMaker AI linear learner built-in algorithm with a value of multiclass_classifier for the predictor_type hyperparameter. What should the company do to MINIMIZE false positives?

- **A.** Set the value of the weight_decay hyperparameter to zero.
- **B.** Increase the number of training epochs.
- **C.** Increase the value of the target_precision hyperparameter.
- **D.** Change the value of the predictor_type hyperparameter to regressor.

??? success "Reveal Answer"
    **Correct Answer: C**

    C. Increase the value of the target_precision hyperparameter. 71

---

## Question 65

An ML engineer wants to use, prepare, and load data from Amazon S3 for analytics. The ML engineer must run an extract, transform, and load (ETL) job to discover the schema of the data and to store the metadata. Which solution will meet these requirements with the LEAST manual effort?

- **A.** Use AWS Glue to run the ETL job. Use the job to discover the schema and to store the associated metadata in the AWS Glue Data Catalog.
- **B.** Create an Amazon SageMaker Data Wrangler flow to run the ETL job. Use the job to discover the schema and to store the associated metadata in an S3 bucket.
- **C.** Create an ETL pipeline by using Amazon Athena integrated with AWS Step Functions. Use the pipeline to run the ETL job to discover the schema and to store the associated metadata in an S3 bucket.
- **D.** Launch an Amazon EC2 instance that includes the scikit-learn library to run the ETL job. Use the job to discover the schema and to store the associated metadata in Amazon Redshift.

??? success "Reveal Answer"
    **Correct Answer: A**

    A. Use AWS Glue to run the ETL job. Use the job to discover the schema and to store the associated metadata in the AWS Glue Data Catalog. 72

---


# Hands-On Labs

Practical labs to reinforce concepts for the MLA-C01 exam.

## Lab Index

| Lab                                       | Topic                   | Domain   | Difficulty |
| ----------------------------------------- | ----------------------- | -------- | ---------- |
| [Lab 01](lab-01-data-wrangler.md)         | SageMaker Data Wrangler | Domain 1 | Easy       |
| [Lab 02](lab-02-training-job.md)          | SageMaker Training Job  | Domain 2 | Medium     |
| [Lab 03](lab-03-hyperparameter-tuning.md) | Hyperparameter Tuning   | Domain 2 | Medium     |
| [Lab 04](lab-04-endpoint-deployment.md)   | Endpoint Deployment     | Domain 3 | Medium     |
| [Lab 05](lab-05-sagemaker-pipelines.md)   | SageMaker Pipelines     | Domain 3 | Hard       |
| [Lab 06](lab-06-model-monitoring.md)      | Model Monitoring        | Domain 4 | Medium     |

## Prerequisites

Before starting the labs, ensure you have:

1. AWS Account with appropriate permissions
2. AWS CLI configured
3. Python 3.9+ with boto3 installed
4. SageMaker Studio or Notebook instance (optional but recommended)

## Cost Warning

!!! warning "AWS Costs"
These labs will incur AWS costs. To minimize expenses:

    - Use the smallest instance types possible
    - Clean up resources after each lab
    - Use SageMaker Savings Plans if doing multiple labs
    - Stop notebook instances when not in use

## Lab Structure

Each lab follows this structure:

1. **Objective** - What you will learn
2. **Prerequisites** - Required setup
3. **Steps** - Detailed instructions
4. **Verification** - How to verify success
5. **Cleanup** - Resource cleanup instructions
6. **Key Takeaways** - Exam-relevant points

## Getting Started

```bash
# Clone the repository
git clone https://github.com/yourusername/aws-mla-study-notes-and-hands-on-labs.git

# Navigate to labs
cd aws-mla-study-notes-and-hands-on-labs

# Set up Python environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install dependencies
pip install boto3 sagemaker pandas
```

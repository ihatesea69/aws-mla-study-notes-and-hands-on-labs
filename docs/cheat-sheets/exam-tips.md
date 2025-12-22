# Exam Tips

Final preparation tips for the MLA-C01 exam.

## Time Management

- **170 minutes** for **65 questions** = ~2.5 minutes per question
- Flag difficult questions and return later
- Don't spend more than 4 minutes on any single question
- Reserve 15 minutes at the end for review

## Question Strategy

### Read Carefully

- Look for keywords: MOST, LEAST, BEST, MINIMUM, MAXIMUM
- Identify the specific requirement (cost, latency, security, etc.)
- Note any constraints mentioned

### Elimination Process

1. Eliminate obviously wrong answers
2. Compare remaining options against requirements
3. Choose the option that BEST fits ALL requirements

### Common Traps

- Solutions that work but are overly complex
- Options that solve a different problem
- Services that exist but aren't best suited

## Key Topics to Review

### SageMaker (Heavily Tested)

- Training job configuration
- Endpoint types and selection criteria
- Built-in algorithms and use cases
- Pipelines for MLOps
- Model Monitor for drift detection

### Bedrock

- When to use Bedrock vs SageMaker
- Knowledge Bases for RAG
- Guardrails for content filtering
- Fine-tuning capabilities

### Data Preparation

- Glue components (Crawlers, Catalog, ETL)
- Feature Store (Online vs Offline)
- Data formats (Parquet, RecordIO)
- Kinesis for streaming

### Security

- IAM roles for SageMaker
- KMS encryption
- VPC configuration
- Secrets Manager

### Cost Optimization

- Spot Training
- Serverless endpoints
- Auto Scaling
- Instance selection

## Common Question Patterns

### "Which endpoint type..."

Consider:

- Latency requirements
- Payload size
- Traffic pattern
- Cost constraints

### "Which service for data..."

Consider:

- Batch vs streaming
- Transformation complexity
- Storage requirements
- Query patterns

### "How to reduce costs..."

Consider:

- Spot instances
- Serverless options
- Right-sizing
- Auto Scaling

### "How to secure..."

Consider:

- Encryption (KMS)
- Access control (IAM)
- Network isolation (VPC)
- Audit logging (CloudTrail)

## Last Day Checklist

### Review

- [ ] All domain summaries
- [ ] Services comparison chart
- [ ] Instance type guide
- [ ] Practice exam mistakes

### Don't Cram

- [ ] Get good sleep
- [ ] Eat a proper meal
- [ ] Arrive early
- [ ] Bring valid ID

### During Exam

- [ ] Read all options before answering
- [ ] Flag uncertain questions
- [ ] Use all available time
- [ ] Trust your preparation

## Key Formulas/Numbers

| Item                       | Value      |
| -------------------------- | ---------- |
| Passing score              | 720/1000   |
| Scored questions           | 50         |
| Unscored questions         | 15         |
| Real-time endpoint timeout | 60 seconds |
| Async endpoint timeout     | 15 minutes |
| Real-time payload limit    | 6 MB       |
| Async payload limit        | 1 GB       |
| Spot training savings      | Up to 90%  |

## Acronyms to Know

| Acronym | Meaning                           |
| ------- | --------------------------------- |
| HPO     | Hyperparameter Optimization       |
| AMT     | Automatic Model Tuning            |
| MME     | Multi-Model Endpoint              |
| RAG     | Retrieval Augmented Generation    |
| SHAP    | SHapley Additive exPlanations     |
| CI/CD   | Continuous Integration/Deployment |
| IAM     | Identity and Access Management    |
| KMS     | Key Management Service            |
| VPC     | Virtual Private Cloud             |
| ECR     | Elastic Container Registry        |

## Good Luck!

Trust your preparation. You've got this!

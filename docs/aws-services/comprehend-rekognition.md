# Amazon Comprehend and Rekognition

## Amazon Comprehend

Natural Language Processing (NLP) service.

### Key Features

| Feature               | Description                            |
| --------------------- | -------------------------------------- |
| Entity Recognition    | Identify people, places, organizations |
| Sentiment Analysis    | Positive, negative, neutral, mixed     |
| Key Phrases           | Extract important phrases              |
| Language Detection    | Identify language                      |
| PII Detection         | Find personal information              |
| Custom Classification | Train custom models                    |
| Custom Entities       | Train custom NER                       |

### Example Usage

```python
import boto3

comprehend = boto3.client("comprehend")

# Sentiment analysis
response = comprehend.detect_sentiment(
    Text="I love this product! It's amazing.",
    LanguageCode="en"
)
# Returns: {"Sentiment": "POSITIVE", "SentimentScore": {...}}

# Entity detection
response = comprehend.detect_entities(
    Text="Amazon was founded by Jeff Bezos in Seattle.",
    LanguageCode="en"
)
# Returns entities: Amazon (ORGANIZATION), Jeff Bezos (PERSON), Seattle (LOCATION)

# PII detection
response = comprehend.detect_pii_entities(
    Text="My email is john@example.com and phone is 555-1234.",
    LanguageCode="en"
)
```

### Comprehend Medical

Healthcare-specific NLP.

- Medical entity extraction
- RxNorm codes
- ICD-10 codes
- Protected health information (PHI)

---

## Amazon Rekognition

Computer vision service.

### Key Features

| Feature               | Description                   |
| --------------------- | ----------------------------- |
| Object Detection      | Identify objects in images    |
| Face Detection        | Detect and analyze faces      |
| Face Comparison       | Compare faces                 |
| Celebrity Recognition | Identify celebrities          |
| Text Detection        | Extract text from images      |
| Content Moderation    | Detect inappropriate content  |
| Custom Labels         | Train custom object detection |

### Example Usage

```python
import boto3

rekognition = boto3.client("rekognition")

# Label detection
response = rekognition.detect_labels(
    Image={"S3Object": {"Bucket": "bucket", "Name": "image.jpg"}},
    MaxLabels=10,
    MinConfidence=80
)

# Face detection
response = rekognition.detect_faces(
    Image={"S3Object": {"Bucket": "bucket", "Name": "photo.jpg"}},
    Attributes=["ALL"]
)

# Content moderation
response = rekognition.detect_moderation_labels(
    Image={"S3Object": {"Bucket": "bucket", "Name": "image.jpg"}}
)
```

### Video Analysis

```python
# Start video analysis
response = rekognition.start_label_detection(
    Video={"S3Object": {"Bucket": "bucket", "Name": "video.mp4"}},
    NotificationChannel={
        "SNSTopicArn": sns_topic_arn,
        "RoleArn": role_arn
    }
)

# Get results
response = rekognition.get_label_detection(JobId=job_id)
```

## Exam Focus Areas

!!! warning "Key Topics" - Comprehend for text analysis and NLP - Rekognition for image/video analysis - Custom models for domain-specific use cases - Content moderation capabilities - Healthcare-specific Comprehend Medical

# Other ML Services

Quick reference for other ML services covered in the exam.

## Amazon Lex

Conversational AI for chatbots.

| Component   | Description           |
| ----------- | --------------------- |
| Intents     | User goals            |
| Slots       | Parameters to collect |
| Utterances  | Example phrases       |
| Fulfillment | Lambda function       |

## Amazon Polly

Text-to-speech service.

| Feature       | Description             |
| ------------- | ----------------------- |
| Neural voices | Natural-sounding speech |
| SSML          | Speech markup control   |
| Lexicons      | Custom pronunciations   |
| Speech marks  | Timing metadata         |

## Amazon Transcribe

Speech-to-text service.

| Feature        | Description             |
| -------------- | ----------------------- |
| Real-time      | Streaming transcription |
| Batch          | Async processing        |
| Medical        | Healthcare-specific     |
| Call Analytics | Contact center insights |

## Amazon Translate

Neural machine translation.

```python
translate = boto3.client("translate")

response = translate.translate_text(
    Text="Hello world",
    SourceLanguageCode="en",
    TargetLanguageCode="es"
)
# Returns: "Hola mundo"
```

## Amazon Textract

Document text extraction.

| Feature        | Description               |
| -------------- | ------------------------- |
| Text Detection | Extract raw text          |
| Forms          | Key-value pairs           |
| Tables         | Structured tables         |
| Queries        | Answer specific questions |

## Amazon Personalize

Recommendation engine.

| Component | Description                |
| --------- | -------------------------- |
| Datasets  | Users, items, interactions |
| Recipes   | Algorithm types            |
| Solutions | Trained models             |
| Campaigns | Real-time recommendations  |

## Amazon Forecast

Time series forecasting.

| Component     | Description           |
| ------------- | --------------------- |
| Dataset Group | Related datasets      |
| Predictor     | Trained model         |
| Forecast      | Generated predictions |

## Amazon Kendra

Enterprise search with ML.

| Feature          | Description       |
| ---------------- | ----------------- |
| Data Sources     | Connectors        |
| Index            | Search index      |
| Queries          | Natural language  |
| Relevance Tuning | Customize ranking |

## Amazon Fraud Detector

Fraud detection service.

| Component   | Description            |
| ----------- | ---------------------- |
| Event Types | Transaction types      |
| Models      | Fraud detection models |
| Rules       | Business logic         |
| Detectors   | Evaluation endpoints   |

## Amazon A2I (Augmented AI)

Human review workflows.

| Component       | Description      |
| --------------- | ---------------- |
| Flow Definition | Review workflow  |
| Human Task UI   | Review interface |
| Workforce       | Reviewers        |

## Service Selection Guide

| Use Case            | Service               |
| ------------------- | --------------------- |
| Chatbots            | Amazon Lex            |
| Text-to-speech      | Amazon Polly          |
| Speech-to-text      | Amazon Transcribe     |
| Translation         | Amazon Translate      |
| Document processing | Amazon Textract       |
| Recommendations     | Amazon Personalize    |
| Forecasting         | Amazon Forecast       |
| Enterprise search   | Amazon Kendra         |
| Fraud detection     | Amazon Fraud Detector |
| Human review        | Amazon A2I            |

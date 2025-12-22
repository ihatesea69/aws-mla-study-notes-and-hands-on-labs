# AWS Certified Machine Learning Engineer Associate (MLA-C01) Study Notes

[![MkDocs](https://img.shields.io/badge/MkDocs-Material-blue?style=for-the-badge&logo=markdown)](https://squidfunk.github.io/mkdocs-material/)
[![AWS](https://img.shields.io/badge/AWS-MLA--C01-FF9900?style=for-the-badge&logo=amazonaws)](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Comprehensive study notes, hands-on labs, and practice exams for the AWS Certified Machine Learning Engineer Associate exam.

## Exam Overview

| Attribute     | Details                      |
| ------------- | ---------------------------- |
| Exam Code     | MLA-C01                      |
| Duration      | 170 minutes                  |
| Questions     | 65 (50 scored + 15 unscored) |
| Passing Score | 720/1000                     |
| Cost          | $150 USD                     |

## Content Domains

| Domain                                          | Weight |
| ----------------------------------------------- | ------ |
| Domain 1: Data Preparation for ML               | 28%    |
| Domain 2: ML Model Development                  | 26%    |
| Domain 3: Deployment and Orchestration          | 22%    |
| Domain 4: Monitoring, Maintenance, and Security | 24%    |

## Getting Started

### Prerequisites

- Python 3.9+
- Git

### Local Development

```bash
# Clone the repository
git clone https://github.com/ihatesea69/aws-mla-study-notes-and-hands-on-labs.git
cd aws-mla-study-notes-and-hands-on-labs

# Create virtual environment
uv venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install MkDocs
uv pip install mkdocs-material

# Serve locally
mkdocs serve
```

Open http://localhost:8000 in your browser.

### Deploy to GitHub Pages

```bash
mkdocs gh-deploy
```

## Structure

```
docs/
├── index.md                          # Home page
├── exam-overview/                    # Exam details
├── domain-1-data-preparation/        # Domain 1 notes
├── domain-2-model-development/       # Domain 2 notes
├── domain-3-deployment-orchestration/# Domain 3 notes
├── domain-4-monitoring-security/     # Domain 4 notes
├── aws-services/                     # Service reference
├── hands-on-labs/                    # Practical labs
├── practice-exams/                   # Practice questions
└── cheat-sheets/                     # Quick reference
```

## Contributing

Contributions are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.

## Official Resources

- [AWS Exam Guide](https://docs.aws.amazon.com/aws-certification/latest/examguides/machine-learning-engineer-associate-01.html)
- [In-Scope AWS Services](https://docs.aws.amazon.com/aws-certification/latest/examguides/mla-01-in-scope-services.html)
- [AWS Skill Builder](https://explore.skillbuilder.aws/)

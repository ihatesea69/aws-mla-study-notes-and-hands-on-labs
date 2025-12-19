# Contributing to Project Name

Thank you for your interest in contributing to this project. This document provides guidelines and instructions for contributing.

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [How to Contribute](#how-to-contribute)
4. [Development Setup](#development-setup)
5. [Pull Request Process](#pull-request-process)
6. [Style Guidelines](#style-guidelines)

---

## Code of Conduct

This project adheres to a Code of Conduct. By participating, you are expected to uphold this code. Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

---

## Getting Started

### Prerequisites

- Git
- Python 3.11+
- Node.js 20+
- Docker (optional)

### Fork and Clone

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/repository.git
   cd repository
   ```
3. Add upstream remote:
   ```bash
   git remote add upstream https://github.com/original-owner/repository.git
   ```

---

## How to Contribute

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

When creating a bug report, include:

- Clear and descriptive title
- Steps to reproduce the issue
- Expected behavior
- Actual behavior
- Environment details (OS, Python version, etc.)
- Screenshots if applicable

### Suggesting Features

Feature suggestions are welcome. Please provide:

- Clear description of the feature
- Use case and benefits
- Potential implementation approach (optional)

### Code Contributions

1. Check existing issues and pull requests
2. Create an issue to discuss significant changes before implementation
3. Follow the development setup instructions
4. Make changes in a feature branch
5. Submit a pull request

---

## Development Setup

### Backend

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt

# Run tests
pytest
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Running Tests

```bash
# Backend tests
pytest --cov=src tests/

# Frontend tests
cd frontend
npm test
```

---

## Pull Request Process

1. Create a feature branch from `main`:

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following the style guidelines

3. Write or update tests as needed

4. Ensure all tests pass:

   ```bash
   pytest
   npm test
   ```

5. Update documentation if needed

6. Commit with clear, descriptive messages:

   ```bash
   git commit -m "Add feature: description of change"
   ```

7. Push to your fork:

   ```bash
   git push origin feature/your-feature-name
   ```

8. Open a Pull Request with:

   - Clear title and description
   - Reference to related issues
   - Screenshots for UI changes

9. Address review feedback

10. Maintain a clean commit history (squash if needed)

---

## Style Guidelines

### Python

- Follow PEP 8 style guide
- Use type hints
- Maximum line length: 100 characters
- Use docstrings for functions and classes

```python
def function_name(param: str) -> dict:
    """
    Brief description of function.

    Args:
        param: Description of parameter.

    Returns:
        Description of return value.
    """
    pass
```

### TypeScript/JavaScript

- Use ESLint configuration
- Use TypeScript for type safety
- Follow functional programming patterns where appropriate

### Git Commit Messages

- Use present tense ("Add feature" not "Added feature")
- Use imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit first line to 72 characters
- Reference issues and pull requests after the first line

```
Add user authentication feature

- Implement JWT token handling
- Add login and logout endpoints
- Create user session management

Fixes #123
```

### Documentation

- Update README.md for user-facing changes
- Add inline comments for complex logic
- Keep documentation concise and accurate

---

## Questions

If you have questions, please:

1. Check existing documentation
2. Search closed issues
3. Open a new issue with the "question" label

Thank you for contributing.

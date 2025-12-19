# Deployment Guide

## Pre-requisites

- Docker
- AWS CLI
- Terraform

## Local Deployment

1. Build the containers:

   ```bash
   docker-compose build
   ```

2. Start the services:
   ```bash
   docker-compose up
   ```

## Production Deployment (AWS)

1. Configure AWS credentials:

   ```bash
   aws configure
   ```

2. Initialize Terraform:

   ```bash
   cd infrastructure
   terraform init
   ```

3. Apply infrastructure changes:
   ```bash
   terraform apply
   ```

## CI/CD Pipeline

Describe your CI/CD pipeline here (e.g., GitHub Actions, Jenkins).

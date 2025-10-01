# DevOps CI/CD on AWS EKS (Blue-Green)

This project provisions an EKS cluster with Terraform and deploys a containerised Flask app via GitHub Actions CI/CD to ECR/EKS using a blue-green strategy.

## What it demonstrates
- Terraform IaC (VPC, EKS, ECR, IAM OIDC for GitHub)
- GitHub Actions OIDC → AWS (no long-lived keys)
- Docker + Kubernetes deployments
- Blue-green switchover via Kubernetes Service selector

## Quick start
```bash
cd infrastructure
terraform init
terraform apply

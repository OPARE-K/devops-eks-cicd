# 🚀 DevOps CI/CD on AWS EKS with Blue/Green Deployments

This project demonstrates a **production-grade CI/CD pipeline** deploying a containerized app on **Amazon EKS** using **Terraform, GitHub Actions, Docker, and Kubernetes**. It follows a **Blue/Green deployment strategy** to ensure zero-downtime rollouts.

---

## 📦 Features
- Infrastructure as Code with **Terraform**
- **Amazon EKS** cluster with managed node groups
- **Amazon ECR** for container image storage
- **GitHub Actions** CI/CD pipeline with OIDC authentication
- **Dockerized application** deployed to Kubernetes
- **Blue/Green Deployment** strategy for safe rollouts
- Public **LoadBalancer Service** exposing the app

---

## 🏗 Architecture

![architecture](./docs/architecture-diagram.png)

**Flow:**
1. Developer pushes code → GitHub Actions triggers.
2. GitHub Actions builds Docker image, pushes to ECR.
3. Pipeline deploys new image as Green deployment.
4. Health check runs on Green.
5. Service flips from Blue → Green if successful.
6. Blue is scaled down (optional).

---

## ⚙️ Tech Stack
- **AWS EKS**
- **Terraform**
- **Docker**
- **Kubernetes (kubectl)**
- **GitHub Actions**
- **Amazon ECR**

---

## 🔑 Secrets Configuration
Set the following in your GitHub Repo → Settings → Secrets and Variables → Actions:

- `AWS_ROLE_TO_ASSUME` → IAM role ARN (from Terraform output `oidc_role_arn`)  
- `AWS_REGION` → e.g., `eu-west-2`  
- `ECR_REPO` → ECR repo URL (from Terraform output `ecr_repo`)  

---

## ▶️ Usage

### 1. Provision Infrastructure
```bash
cd infrastructure
terraform init
terraform apply -auto-approve

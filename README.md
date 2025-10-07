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



---

## 📈 Monitoring & Observability Demo

This environment integrates a **Prometheus + Grafana** monitoring stack using the `kube-prometheus-stack` Helm chart.

It provides real-time metrics, visual dashboards, and alerting for both the Kubernetes cluster and the deployed application.

---

### 🧩 Stack Overview

| Component | Purpose |
|------------|----------|
| **Prometheus** | Scrapes metrics from cluster and app targets |
| **Grafana** | Visualizes metrics and dashboards |
| **Alertmanager** | Routes alerts from Prometheus rules |
| **ServiceMonitor** | Custom resource to tell Prometheus which app endpoints to scrape |

---

### 📊 Grafana — Kubernetes Cluster Overview

Shows cluster node health, CPU/memory usage, and pod counts.

![Grafana Cluster Dashboard](screenshots/grafana-cluster.png)

---

### 🧩 Grafana — Application (web-green) Pod Metrics

Pod-level CPU/memory stats and request throughput for the running web deployment.

![Grafana Web Pod Metrics](screenshots/grafana-web-pods.png)

---

### 🎯 Prometheus — Targets Page

Prometheus automatically discovered all service monitors, including the custom `web` ServiceMonitor target.

![Prometheus Targets](screenshots/prometheus-targets.png)

---

### 📉 Prometheus — Request Count & Probe Success

Demonstrates collected app metrics and blackbox probes.

- **`web_requests_total`** → HTTP requests handled by the app  
- **`probe_success`** → External availability check for ELB endpoint

![Prometheus Metrics Graph](screenshots/prometheus-graph.png)

---

### 🚨 Prometheus — Alert Rules & Triggered Alerts

Alerts for high error rate or downtime.  
Here, `WebHighErrorRate` fired when the app returned HTTP 500s.

![Prometheus Alerts](screenshots/prometheus-alerts.png)

---

### 🕵️‍♂️ Blackbox Exporter — Service Availability

Validates that the public endpoint is reachable (HTTP 200 = success).

![Blackbox Probe Result](screenshots/probe-success.png)

---

### 🧾 Summary

| Area | Tool | Example Metric / Purpose |
|------|------|---------------------------|
| Cluster Health | Grafana | CPU, memory, pod count |
| App Performance | Prometheus | `web_requests_total`, latency |
| Service Availability | Blackbox | `probe_success` |
| Alerting | Prometheus / Alertmanager | High error rate, downtime |

---

### 🧠 Key Learnings

- Built **end-to-end observability** into a CI/CD-managed EKS app  
- Exposed custom app metrics with the **prometheus-client** library  
- Automated scraping using **ServiceMonitor** CRDs  
- Integrated **blackbox probing** for uptime visibility  
- Triggered and resolved **custom alert rules**

---

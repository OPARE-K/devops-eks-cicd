📘 Part 2 — “Monitoring Demo Walkthrough” Documentation Page

You can save this as docs/monitoring-demo.md or merge it into your README.
It reads like a post-deployment report (which recruiters and interviewers love).

🧩 Monitoring Demo Walkthrough
Objective

To demonstrate observability and proactive monitoring for a Kubernetes-based web app deployed via CI/CD on AWS EKS.

Environment Summary
Component	Description
Cloud Provider	AWS (EKS, ECR, IAM, CloudWatch for cluster logs)
CI/CD Pipeline	GitHub Actions deploying blue/green to EKS
Monitoring Stack	Prometheus, Grafana, Alertmanager via Helm
Application Metrics	Exposed via /metrics endpoint (Prometheus format)
Alert Rules	Custom PromQL thresholds for latency and errors
Blackbox Probes	External HTTP checks against public ELB endpoint
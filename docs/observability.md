# Observability guide

## Metrics
Each service exports Prometheus counters at `/metrics`. The starter dashboard visualizes request rates. In production, add latency histograms, error rates, saturation, and business metrics.

## Local Prometheus
The provided `prometheus.yml` assumes Compose DNS names. To run Prometheus locally, add a Prometheus service to Compose and mount this file at `/etc/prometheus/prometheus.yml`.

## Grafana
Import `monitoring/grafana-dashboard.json`. Select the Prometheus data source and validate queries against your metric labels.

## AWS EKS
For a real cluster:
- Install the AWS CloudWatch Observability add-on or Fluent Bit for logs.
- Use kube-prometheus-stack or Amazon Managed Prometheus for metrics.
- Use Amazon Managed Grafana or self-managed Grafana.
- Alert on availability, error rate, latency, restarts, CPU/memory saturation, and failed rollout.
- Avoid putting secrets, tokens, email addresses, or personal data in labels/logs.

# Architecture and design decisions

## Boundaries
- `user-service`, `product-service`, and `order-service` are separately built and versioned.
- Each service exposes health/readiness endpoints and Prometheus metrics.
- Helm packages deployments and services with reusable values.
- Terraform provisions a sandbox EKS foundation; CloudFormation demonstrates a separate ECR resource.
- CI scans source/configuration and each built container image before a release can proceed.

## Security controls
- Containers run as a non-root user.
- Kubernetes pods disable privilege escalation, drop capabilities, use read-only root filesystems and RuntimeDefault seccomp.
- Kubernetes workloads have CPU/memory requests and limits, plus liveness/readiness probes.
- Trivy blocks the pipeline for HIGH/CRITICAL findings by default. Findings should be triaged; never suppress a finding without a documented reason.
- Use immutable image tags (commit SHA or release version), short-lived cloud credentials via OIDC, least-privilege IAM, and protected deployment environments.
- Do not commit `.env`, cloud credentials, kubeconfigs, Terraform state, or real customer data.

## Known demo limitations
- Data is in-memory and resets when a process restarts.
- Services do not yet call one another; service-to-service authentication and authorization must be added if cross-service calls are introduced.
- Prometheus configuration is a local Docker Compose example. EKS needs service discovery/operator configuration.
- The chart's default-deny ingress NetworkPolicy intentionally blocks ingress unless explicit allow policies are added. Add carefully scoped rules before exposing workloads.
- No public ingress/load balancer is configured in the chart by default.

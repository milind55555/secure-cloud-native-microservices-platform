# Agile backlog and sprint plan

## Epic: Secure microservices delivery
**Definition of Done:** reviewed code, tests pass, security gates pass, versioned artifact, deployment validated, runbook updated.

### Sprint 1 — Service foundation
- [ ] Create three independently testable APIs
- [ ] Add health/readiness/metrics endpoints
- [ ] Containerize services as non-root
- [ ] Add API tests and local Compose workflow

### Sprint 2 — Secure CI
- [ ] Add GitHub Actions test workflow
- [ ] Add Trivy filesystem and image scans
- [ ] Configure SonarQube project and quality gate
- [ ] Publish SBOM and archive scan reports

### Sprint 3 — Kubernetes and cloud
- [ ] Review Terraform plan and provision sandbox EKS
- [ ] Deploy services through Helm
- [ ] Configure registry, image retention, and immutable tags
- [ ] Test rollout status and rollback

### Sprint 4 — Operations
- [ ] Configure Prometheus and Grafana
- [ ] Ship logs to CloudWatch
- [ ] Run a simulated failed release and document recovery
- [ ] Complete architecture review and demo

## Example issue template
**Problem:**  
**Acceptance criteria:**  
**Risk/security considerations:**  
**Test evidence:**  
**Owner:**  
**Target sprint:**  

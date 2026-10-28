# Validation checklist

- [ ] `docker compose up --build` starts all services
- [ ] All `/health`, `/ready`, and sample endpoints return expected responses
- [ ] `pytest -q` passes
- [ ] GitHub Actions runs on a pull request
- [ ] Trivy findings reviewed and addressed; no secrets committed
- [ ] `helm lint helm/secure-platform` succeeds
- [ ] `helm template secure-platform helm/secure-platform` output reviewed
- [ ] Terraform `fmt`, `validate`, and `plan` reviewed in a sandbox account
- [ ] EKS deployment reaches readiness
- [ ] Rollback tested and recorded
- [ ] Dashboard queries validated against real metrics
- [ ] CloudWatch logs and alerts verified
- [ ] README contains your own screenshots and truthful implementation status

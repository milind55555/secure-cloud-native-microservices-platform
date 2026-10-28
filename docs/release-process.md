# Release and rollback process

## Versioning
1. Use semantic release versions (for example `1.0.0`) and retain commit SHA tags for traceability.
2. Build once; promote the same immutable image digest between environments.
3. Store images in ECR or Artifactory. Do not overwrite release tags.
4. Record the Git commit, scan output, test results, approval, and deployment timestamp in the release ticket.

## Promotion checklist
- [ ] Pull request reviewed and CI green
- [ ] Unit tests pass
- [ ] Trivy filesystem and image scans reviewed; no unapproved HIGH/CRITICAL findings
- [ ] SonarQube quality gate passed, if configured
- [ ] Image pushed to approved registry and digest recorded
- [ ] Helm template/lint validated
- [ ] Change ticket and rollback version recorded
- [ ] Protected environment approval completed

## Deploy
```bash
helm lint helm/secure-platform
helm upgrade --install secure-platform helm/secure-platform -n secure-platform --create-namespace
kubectl rollout status deployment/user-service -n secure-platform
kubectl rollout status deployment/product-service -n secure-platform
kubectl rollout status deployment/order-service -n secure-platform
```

## Roll back
```bash
helm history secure-platform -n secure-platform
helm rollback secure-platform <REVISION> -n secure-platform
kubectl get pods -n secure-platform
kubectl get events -n secure-platform --sort-by=.lastTimestamp
```

## Rollback triggers
Rollback when error rate, latency, crash loops, failed readiness checks, or customer-impacting behavior exceeds the team's agreed threshold. Record evidence and notify the service owner.

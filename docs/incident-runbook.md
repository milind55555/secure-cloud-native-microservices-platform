# Incident response runbook

## 1. Triage
- Declare incident severity using the team's severity matrix.
- Identify impacted service, namespace, release revision, and start time.
- Assign incident lead, communications owner, and technical investigator.
- Preserve relevant logs, events, metrics, and deployment history.

## 2. Initial Kubernetes checks
```bash
kubectl get pods -n secure-platform -o wide
kubectl get deployments,services -n secure-platform
kubectl get events -n secure-platform --sort-by=.lastTimestamp
kubectl describe deployment user-service -n secure-platform
kubectl logs deployment/user-service -n secure-platform --all-containers=true --tail=200
```

## 3. Common scenarios
### Pods not ready
Check image pull errors, probe paths/ports, resource pressure, service selectors, and NetworkPolicy rules.

### CrashLoopBackOff
Inspect previous logs (`kubectl logs <pod> --previous`), config, memory limits, and startup exceptions. Do not paste secrets into tickets.

### New release causes errors
Compare current and previous image digests, inspect rollout history, and roll back using `helm rollback`.

### Vulnerability discovered
Identify affected image digest and deployed workloads, assess exploitability, notify the owner, patch/rebuild, rescan, and redeploy. Keep an audit trail.

## 4. Recovery and closure
- Verify readiness and key API endpoints.
- Confirm dashboards return to expected behavior.
- Communicate service restoration.
- Write a blameless post-incident review: timeline, impact, root cause, contributing factors, what went well, corrective actions, owners, and due dates.

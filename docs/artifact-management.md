# Artifact and container image management

## Suggested Artifactory repositories
- `pypi-virtual`: virtual Python package repository for dependency resolution.
- `docker-local`: local Docker repository for built images.
- `generic-local`: optional repository for signed release manifests and SBOMs.

Configure the JFrog CLI or Docker client using CI secrets, never literal credentials. Prefer OIDC/workload identity when supported.

## Image tags and traceability
Use tags like `1.0.0` and `sha-<full-commit>`. Configure immutable release tags, retention policies, access controls, and audit logs. Promote by digest instead of rebuilding.

## Example commands (adapt to your Artifactory hostname)
```bash
docker login YOUR_ARTIFACTORY_HOST
docker tag local/user-service:BUILD_TAG YOUR_ARTIFACTORY_HOST/docker-local/user-service:BUILD_TAG
docker push YOUR_ARTIFACTORY_HOST/docker-local/user-service:BUILD_TAG
```

Do not use `latest` as the sole production identifier. Do not store passwords in shell history or repository files.

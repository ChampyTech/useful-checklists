# ✅ GitHub Actions Setup Checklist

↖️ [Return to the main file](../README.md)

### Workflow Basics
- [ ] Create `.github/workflows/` directory
- [ ] Define clear workflow names
- [ ] Add triggers (push, pull_request, schedule, etc.)

### Job Configuration
- [ ] Specify the right `runs-on` environment (ubuntu-latest, windows-latest, etc.)
- [ ] Define multiple jobs if needed (build, test, deploy)
- [ ] Use caching for dependencies to speed up workflows

### Secrets & Security
- [ ] Store tokens and credentials in GitHub Secrets
- [ ] Avoid hardcoding sensitive values in workflows
- [ ] Limit permissions for `GITHUB_TOKEN`
- [ ] Review third-party Actions before use

### Optimization & Maintenance
- [ ] Reuse workflows with `workflow_call`
- [ ] Keep Actions updated to latest versions
- [ ] Remove unused workflows
- [ ] Monitor execution times and costs
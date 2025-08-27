# ✅ GitHub Repository Security Checklist

↖️ [Return to the main file](../README.md)

### Access Control
- [ ] Restrict admin permissions only to trusted collaborators
- [ ] Enable branch protection rules (main/master branch)
- [ ] Require pull request reviews before merging
- [ ] Remove inactive collaborators

### Authentication & Secrets
- [ ] Enforce 2FA (two-factor authentication) for all contributors
- [ ] Never commit secrets (API keys, passwords) to the repository
- [ ] Add `.gitignore` for sensitive files
- [ ] Use GitHub Secrets for environment variables

### Dependency Management
- [ ] Enable Dependabot alerts
- [ ] Regularly update dependencies
- [ ] Audit third-party libraries for vulnerabilities

### Monitoring & Policies
- [ ] Set up a SECURITY.md file for reporting vulnerabilities
- [ ] Monitor code scanning alerts
- [ ] Review logs of repository actions
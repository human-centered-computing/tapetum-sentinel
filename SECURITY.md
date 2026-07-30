# Security Policy

Do not publish security vulnerabilities in public issues.

Until a dedicated private reporting channel is configured, contact the repository owner through GitHub with a minimal disclosure request. Do not include sensitive datasets, credentials, access tokens or private video samples in the first message.

## Secrets

- Never commit GitHub or Hugging Face tokens.
- Use `.env` files locally and repository secrets in CI.
- Rotate any token that is accidentally exposed.

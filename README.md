# flask-pwa-demo
A flask progressive web app teaching repository

# This is a teaching tool for students in Stage 5 Computing Technology and Stage 6 Software Engineering.
The NSW Department of Education places certain security restrictions upon student desktops.

This project uses the following tools to provide an authentic example of industry procedure in software development:
- Github
- Github Codespaces
- Docker containerisation

## Security notes and rationale
- Talisman sets secure headers including HSTS and a Content Security Policy to reduce XSS risk.

- CSRF protection via Flask-WTF is enabled by CSRFProtect.

- Rate limiting via Flask-Limiter reduces brute force and scraping risk.

- Password hashing uses passlib[bcrypt] for strong, salted hashes.

- Non-root container reduces blast radius if the container is compromised.

- Dev tooling (bandit, pip-audit, safety) runs locally and in CI to catch code and dependency issues early.

- Instance folder keeps secrets and local DB out of source control; CI should populate instance files from a vault.

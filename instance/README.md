This folder contains runtime overrides and secrets for local/dev.
- Keep this folder in .gitignore
- CI should populate instance/.env or instance/config.py from a secrets manager
- Do not store long-lived production secrets here; use a vault in production

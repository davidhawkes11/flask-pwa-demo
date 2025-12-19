# instance/config.py  -- DO NOT COMMIT
# Small overrides loaded by Flask when instance exists

SECRET_KEY = "replace-with-vault-secret"
SQLALCHEMY_DATABASE_URI = "sqlite:///instance/app.sqlite3"
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
WTF_CSRF_ENABLED = True

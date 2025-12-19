from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from flask_talisman import Talisman
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import ProductionConfig, DevelopmentConfig
import os

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
login_manager = LoginManager()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per day", "50 per hour"])

def create_app(config_name=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load base config then instance overrides
    env = os.environ.get("FLASK_ENV", "production")
    if env == "development":
        app.config.from_object(DevelopmentConfig)
    else:
        app.config.from_object(ProductionConfig)
    app.config.from_pyfile("config.py", silent=True)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    limiter.init_app(app)

    # Security headers and CSP via Talisman
    csp = app.config.get("CSP", {})
    Talisman(app, content_security_policy=csp, force_https=not app.debug, strict_transport_security=True)

    # Register blueprints or routes
    from . import routes
    app.register_blueprint(routes.bp)

    return app

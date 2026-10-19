"""
Flask extensions initialization.

We create them here without an app, then bind them to the app
in the application factory (create_app).
"""

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
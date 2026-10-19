from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()

# Set up Login Manager for authentication
login_manager = LoginManager()
# If an unauthenticated user tries to access a protected page,
# redirect them to the 'admin.login' route
login_manager.login_view = 'admin.login'
login_manager.login_message_category = 'error'
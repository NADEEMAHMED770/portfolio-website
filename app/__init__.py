"""
Application factory for the portfolio website.
"""

from flask import Flask, render_template
from config import config

# Import all extensions
from app.extensions import db, migrate, login_manager, csrf


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register blueprints
    from app.blueprints.main import main_bp
    from app.blueprints.admin import admin_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    # Setup Flask-Login user loader
    @login_manager.user_loader
    def load_user(user_id):
        from app.models import User
        return User.query.get(int(user_id))

    # Register error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    # Health check
    @app.route('/_health')
    def health_check():
        return {'status': 'ok', 'version': '0.5.0'} # Updated to 0.5.0

    # Import models so Flask-Migrate detects them
    from app import models

    return app
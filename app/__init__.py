"""
Application factory for the portfolio website.
"""

from flask import Flask, render_template
from config import config
from app.extensions import db, migrate  # <-- Import extensions


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

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
        return {'status': 'ok', 'version': '0.4.0'}

    # Import models so Flask-Migrate detects them
    from app import models

    return app
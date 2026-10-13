"""
Application factory for the portfolio website.

This module defines `create_app()`, which builds and configures the Flask
application. Every entry point (run.py, tests, CLI commands) uses this
function — never a global `app` object.
"""

from flask import Flask
from config import config


def create_app(config_name='development'):
    """
    Create and configure a Flask application instance.

    Args:
        config_name (str): One of 'development', 'production', 'testing'.

    Returns:
        Flask: A configured Flask app ready to handle requests.
    """
    app = Flask(__name__)

    # --- Load configuration ---
    app.config.from_object(config[config_name])

    # --- Register blueprints ---
    from app.blueprints.main import main_bp
    app.register_blueprint(main_bp)

    # --- Health check route (proves the app works) ---
    @app.route('/_health')
    def health_check():
        """Simple health check — used by monitoring and CI."""
        return {'status': 'ok', 'version': '0.1.0'}

    return app
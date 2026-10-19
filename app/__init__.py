"""
Application factory for the portfolio website.

This module defines `create_app()`, which builds and configures the Flask
application. Every entry point (run.py, tests, CLI commands) uses this
function — never a global `app` object.
"""

from flask import Flask, render_template  # <--- Added render_template here
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

    # --- Temporary route to test 500 error page ---
    @app.route('/_force-500')
    def force_500():
        raise Exception("Testing 500 error")

    # --- Register error handlers ---
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    # --- Health check route (proves the app works) ---
    @app.route('/_health')
    def health_check():
        """Simple health check — used by monitoring and CI."""
        return {'status': 'ok', 'version': '0.2.0'} # Updated version to 0.2.0

    return app
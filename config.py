"""
Configuration classes for the portfolio website.

Three environments:
- DevelopmentConfig  → local development (DEBUG=True, SQLite)
- ProductionConfig   → deployed to Render (DEBUG=False, PostgreSQL)
- TestingConfig      → pytest runs (isolated DB, no CSRF)

Used via:
    from config import config
    app.config.from_object(config['development'])
"""

import os
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent


class Config:
    """Base configuration — shared across all environments."""

    # --- Flask Core ---
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-CHANGE-IN-PRODUCTION'

    # --- Database ---
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{BASE_DIR / "instance" / "portfolio.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Security ---
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'

    # --- Pagination ---
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(Config):
    """Local development — verbose errors, debug mode on."""

    DEBUG = True
    TESTING = False
    ENV = 'development'


class ProductionConfig(Config):
    """Production — errors hidden, secure cookies, real DB."""

    DEBUG = False
    TESTING = False
    ENV = 'production'

    # Force secure cookies in production
    SESSION_COOKIE_SECURE = True
    REMEMBER_COOKIE_SECURE = True


class TestingConfig(Config):
    """Testing — isolated, fast, no CSRF, in-memory DB."""

    DEBUG = False
    TESTING = True
    ENV = 'testing'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False


# Registry — used by create_app()
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
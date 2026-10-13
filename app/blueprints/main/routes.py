"""
Routes for the main blueprint.

V0.1 — skeleton routes only. Real pages come in V0.2.
"""

from flask import render_template
from app.blueprints.main import main_bp


@main_bp.route('/')
def home():
    """Homepage — the primary landing page."""
    return render_template('main/index.html', page_title='Home')


@main_bp.route('/about')
def about():
    """About page — placeholder for V0.2."""
    return '<h1>About</h1><p>Coming in V0.2.</p>'


@main_bp.route('/projects')
def projects():
    """Projects list — placeholder for V0.2."""
    return '<h1>Projects</h1><p>Coming in V0.2.</p>'
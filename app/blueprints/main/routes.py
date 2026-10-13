"""
Routes for the main blueprint.

V0.2 — Real template rendering. Content still hardcoded; database integration in V0.4.
"""

from flask import render_template
from app.blueprints.main import main_bp


@main_bp.route('/')
def home():
    """Homepage — hero, featured projects, skills, education."""
    return render_template('main/home.html', page_title='Home')


@main_bp.route('/about')
def about():
    """About page — full bio, current focus, languages."""
    return '<h1>About</h1><p>Coming in V0.2b.</p>', 200


@main_bp.route('/projects')
def projects():
    """Projects list — all projects with filters."""
    return '<h1>Projects</h1><p>Coming in V0.2b.</p>', 200


@main_bp.route('/education')
def education():
    """Education page — university, CGPA, courses."""
    return '<h1>Education</h1><p>Coming in V0.2b.</p>', 200


@main_bp.route('/certifications')
def certifications():
    """Certifications and courses."""
    return '<h1>Certifications</h1><p>Coming in V0.2b.</p>', 200


@main_bp.route('/contact')
def contact():
    """Contact page — form and social links."""
    return '<h1>Contact</h1><p>Coming in V0.2b.</p>', 200
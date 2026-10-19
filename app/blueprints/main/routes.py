"""
Routes for the main blueprint.
"""

from flask import render_template
from app.blueprints.main import main_bp


@main_bp.route('/')
def home():
    return render_template('main/home.html', page_title='Home')


@main_bp.route('/about')
def about():
    return render_template('main/about.html', page_title='About')


@main_bp.route('/projects')
def projects():
    return render_template('main/projects.html', page_title='Projects')


@main_bp.route('/education')
def education():
    return render_template('main/education.html', page_title='Education')


@main_bp.route('/certifications')
def certifications():
    return render_template('main/certifications.html', page_title='Certifications')


@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html', page_title='Contact')
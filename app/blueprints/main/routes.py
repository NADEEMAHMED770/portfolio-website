"""
Routes for the main blueprint.
"""

from flask import render_template
from app.blueprints.main import main_bp
from app.models import Profile, Project, Skill, Education, Certification


@main_bp.route('/')
def home():
    profile = Profile.query.first()
    projects = Project.query.filter_by(is_featured=True).order_by(Project.display_order).limit(4).all()
    
    # FIX: Order by category, then display order, and remove the limit
    skills = Skill.query.filter_by(is_learning=False).order_by(Skill.category, Skill.display_order).all()
    
    education = Education.query.filter_by(is_current=True).first()

    return render_template(
        'main/home.html', 
        page_title='Home',
        profile=profile,
        projects=projects,
        skills=skills,
        education=education
    )


@main_bp.route('/about')
def about():
    profile = Profile.query.first()
    return render_template('main/about.html', page_title='About', profile=profile)


@main_bp.route('/projects')
def projects():
    all_projects = Project.query.order_by(Project.display_order).all()
    return render_template('main/projects.html', page_title='Projects', projects=all_projects)


@main_bp.route('/education')
def education():
    edu = Education.query.filter_by(is_current=True).first()
    return render_template('main/education.html', page_title='Education', education=edu)


@main_bp.route('/certifications')
def certifications():
    certs = Certification.query.all()
    return render_template('main/certifications.html', page_title='Certifications', certifications=certs)


@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html', page_title='Contact')
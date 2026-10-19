"""
Database Models for the Portfolio Website.

Defines the schema using SQLAlchemy.
"""

from datetime import datetime
from app.extensions import db


class User(db.Model):
    """Admin user model."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'


class Profile(db.Model):
    """Single-row table for personal branding."""
    __tablename__ = 'profile'
    
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    tagline = db.Column(db.String(200), nullable=True)
    short_bio = db.Column(db.Text, nullable=True)
    long_bio = db.Column(db.Text, nullable=True)
    city = db.Column(db.String(80), nullable=True)
    province = db.Column(db.String(80), nullable=True)
    country = db.Column(db.String(80), nullable=True)
    available_for_hire = db.Column(db.Boolean, default=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class Education(db.Model):
    """University and degree information."""
    __tablename__ = 'education'
    
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(200), nullable=False)
    short_name = db.Column(db.String(80), nullable=True)
    degree = db.Column(db.String(120), nullable=False)
    department = db.Column(db.String(120), nullable=True)
    start_year = db.Column(db.Integer, nullable=False)
    end_year = db.Column(db.Integer, nullable=True)
    current_semester = db.Column(db.Integer, nullable=True)
    cgpa = db.Column(db.Float, nullable=True)
    cgpa_scale = db.Column(db.Float, default=4.0)
    is_current = db.Column(db.Boolean, default=True)
    display_order = db.Column(db.Integer, default=0)


class Skill(db.Model):
    """Skills and proficiency levels."""
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    level = db.Column(db.String(20), nullable=False)
    is_learning = db.Column(db.Boolean, default=False)
    display_order = db.Column(db.Integer, default=0)


class Project(db.Model):
    """Portfolio projects."""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(120), unique=True, nullable=False)
    title = db.Column(db.String(150), nullable=False)
    one_liner = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    tech_stack = db.Column(db.String(300), nullable=True)
    role = db.Column(db.String(100), nullable=True)
    github_url = db.Column(db.String(300), nullable=True)
    live_url = db.Column(db.String(300), nullable=True)
    status = db.Column(db.String(30), default='completed')
    is_featured = db.Column(db.Boolean, default=False)
    display_order = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Project {self.title}>'


class Certification(db.Model):
    """Certifications and courses."""
    __tablename__ = 'certifications'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    issuer = db.Column(db.String(120), nullable=False)
    issue_date = db.Column(db.Date, nullable=False)
    verification_url = db.Column(db.String(300), nullable=True)
    display_order = db.Column(db.Integer, default=0)
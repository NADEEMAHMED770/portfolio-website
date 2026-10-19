from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from app.blueprints.admin import admin_bp
from app.models import User, Project
from app.forms import LoginForm, ProjectForm
from app.extensions import db
import os
from werkzeug.utils import secure_filename
from flask import current_app

@admin_bp.route('/')
@login_required
def dashboard():
    return render_template('admin/dashboard.html')

@admin_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('admin.dashboard'))
        
    form = LoginForm()
    
    if form.validate_on_submit():
        # Find user by email
        user = User.query.filter_by(email=form.email.data).first()
        
        # Check if user exists AND password is correct
        if user is None or not user.check_password(form.password.data):
            flash('Invalid email or password.', 'error')
            return redirect(url_for('admin.login'))
            
        # Log the user in
        login_user(user, remember=True)
        
        # Handle the "next" page (if they were redirected from a protected route)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('admin.dashboard')
            
        flash('You have been logged in.', 'success')
        return redirect(next_page)
        
    return render_template('admin/login.html', form=form)

@admin_bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('main.home'))

# ==========================================
# PROJECT CRUD
# ==========================================

@admin_bp.route('/projects')
@login_required
def projects():
    all_projects = Project.query.order_by(Project.display_order).all()
    return render_template('admin/projects.html', projects=all_projects)

@admin_bp.route('/projects/create', methods=['GET', 'POST'])
@login_required
def project_create():
    form = ProjectForm()
    if form.validate_on_submit():
        project = Project(
            title=form.title.data,
            slug=form.slug.data,
            one_liner=form.one_liner.data,
            description=form.description.data,
            tech_stack=form.tech_stack.data,
            role=form.role.data,
            github_url=form.github_url.data,
            live_url=form.live_url.data,
            is_featured=form.is_featured.data
        )
        
        # --- NEW: Handle Image Upload ---
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            # Save file to: app/static/uploads/projects/
            upload_path = os.path.join(current_app.root_path, 'static/uploads/projects', filename)
            form.image.data.save(upload_path)
            project.image_file = filename
        # --------------------------------
            
        db.session.add(project)
        db.session.commit()
        flash('Project created successfully.', 'success')
        return redirect(url_for('admin.projects'))
    return render_template('admin/project_form.html', form=form, action="Create")


@admin_bp.route('/projects/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def project_edit(id):
    project = Project.query.get_or_404(id)
    form = ProjectForm(obj=project)
    
    if form.validate_on_submit():
        # --- NEW: Handle Image Upload ---
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            upload_path = os.path.join(current_app.root_path, 'static/uploads/projects', filename)
            form.image.data.save(upload_path)
            project.image_file = filename
        # --------------------------------
            
        # Update all other fields
        form.populate_obj(project)
        # Note: populate_obj might overwrite image_file with the FileStorage object if we don't fix it.
        # To be safe, we reassign the filename if it was updated:
        if form.image.data:
            project.image_file = secure_filename(form.image.data.filename)

        db.session.commit()
        flash('Project updated successfully.', 'success')
        return redirect(url_for('admin.projects'))
        
    return render_template('admin/project_form.html', form=form, action="Edit")
@admin_bp.route('/projects/delete/<int:id>', methods=['POST'])
@login_required
def project_delete(id):
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    flash('Project deleted.', 'success')
    return redirect(url_for('admin.projects'))
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user, login_user, logout_user
from app.blueprints.admin import admin_bp
from app.models import User
from app.forms import LoginForm

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
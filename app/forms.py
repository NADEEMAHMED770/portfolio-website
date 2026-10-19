from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed
from wtforms import SelectField

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, URL, Optional

# ... (keep LoginForm) ...

class ProjectForm(FlaskForm):
    title = StringField('Project Title', validators=[DataRequired()])
    slug = StringField('URL Slug (e.g., my-cool-project)', validators=[DataRequired()])
    one_liner = StringField('One-Liner', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Optional()])
    tech_stack = StringField('Tech Stack (comma separated, e.g., Python, Flask, ML)', validators=[Optional()])
    role = StringField('Your Role', validators=[Optional()])
    github_url = StringField('GitHub URL', validators=[Optional(), URL()])
    live_url = StringField('Live Demo URL', validators=[Optional(), URL()])
    is_featured = BooleanField('Feature on Homepage')
    image = FileField('Project Thumbnail', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Save Project')

class SkillForm(FlaskForm):
    name = StringField('Skill Name', validators=[DataRequired()])
    category = SelectField('Category', choices=[
        ('Programming', 'Programming'),
        ('Data Science', 'Data Science'),
        ('Web & Tools', 'Web & Tools'),
        ('Soft Skills', 'Soft Skills'),
        ('Currently Learning', 'Currently Learning')
    ], validators=[DataRequired()])
    level = SelectField('Proficiency', choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    ], validators=[DataRequired()])
    is_learning = BooleanField('Currently Learning?')
    submit = SubmitField('Save Skill')



class EducationForm(FlaskForm):
    institution = StringField('Institution Name', validators=[DataRequired()])
    short_name = StringField('Short Name (for UI)', validators=[Optional()])
    degree = StringField('Degree', validators=[DataRequired()])
    department = StringField('Department', validators=[Optional()])
    start_year = StringField('Start Year', validators=[DataRequired()])
    end_year = StringField('End Year', validators=[Optional()])
    current_semester = StringField('Current Semester', validators=[Optional()])
    cgpa = StringField('CGPA', validators=[Optional()])
    cgpa_scale = StringField('CGPA Scale (e.g., 4.0)', validators=[Optional()], default="4.0")
    is_current = BooleanField('Currently Studying Here?', default=True)
    submit = SubmitField('Save Education')
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileAllowed

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
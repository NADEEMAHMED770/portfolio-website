from app import create_app
from app.extensions import db
from app.models import User

app = create_app('development')

with app.app_context():
    # Check if user exists
    user = User.query.filter_by(email='nadeemahmedghoto06@gmail.com').first()
    if user:
        print("User already exists!")
    else:
        user = User(email='nadeemahmedghoto06@gmail.com')
        user.set_password('MySuperSecretPassword123!') # Change this!
        db.session.add(user)
        db.session.commit()
        print("Admin user created successfully!")
"""
Seed script to populate the database with initial data.
Run this via: python seed.py
"""
from datetime import date
from app import create_app
from app.extensions import db
from app.models import Profile, Education, Skill, Project, Certification

app = create_app('development')

def seed_database():
    with app.app_context():
        print("Clearing existing data...")
        db.session.query(Certification).delete()
        db.session.query(Project).delete()
        db.session.query(Skill).delete()
        db.session.query(Education).delete()
        db.session.query(Profile).delete()
        db.session.commit()

        print("Adding Profile...")
        profile = Profile(
            full_name="Nadeem Ahmed Ghoto",
            title="AI/ML Student & Aspiring Engineer",
            tagline="Aspiring AI/ML Engineer | Learning Python & Data Analytics | Building projects from scratch.",
            city="Ghotki",
            province="Sindh",
            country="Pakistan",
            available_for_hire=True
        )
        db.session.add(profile)

        print("Adding Education...")
        edu = Education(
            institution="Aror University of Art, Architecture, Design & Heritage",
            short_name="Aror University, Sukkur",
            degree="BS Artificial Intelligence",
            department="Emerging Sciences and Technology",
            start_year=2025,
            end_year=2029,
            current_semester=3,
            cgpa=3.58,
            cgpa_scale=4.0,
            is_current=True
        )
        db.session.add(edu)

        print("Adding Skills...")
        skills_data = [
            ("Programming", "Python", "Intermediate"),
            ("Programming", "SQL", "Intermediate"),
            ("Programming", "Java", "Intermediate"),
            ("Data Science", "Pandas", "Intermediate"),
            ("Data Science", "NumPy", "Intermediate"),
            ("Data Science", "scikit-learn", "Beginner"),
            ("Web & Tools", "Flask", "Beginner"),
            ("Web & Tools", "Git", "Intermediate"),
            ("Currently Learning", "Power BI", "Beginner"),
            ("Currently Learning", "Tableau", "Beginner")
        ]
        for cat, name, level in skills_data:
            skill = Skill(category=cat, name=name, level=level, is_learning=(cat=="Currently Learning"))
            db.session.add(skill)

        print("Adding Projects...")
        projects_data = [
            {
                "title": "Car Price Prediction",
                "slug": "car-price-prediction",
                "one_liner": "Flask ML deployment predicting used car prices.",
                "tech_stack": "Python, Flask, ML",
                "role": "Solo",
                "is_featured": True
            },
            {
                "title": "Local Skill Marketplace",
                "slug": "local-skill-marketplace",
                "one_liner": "Java Swing + MySQL desktop application.",
                "tech_stack": "Java, MySQL",
                "role": "Backend & DB",
                "is_featured": True
            },
            {
                "title": "Unemployment Analysis",
                "slug": "unemployment-analysis",
                "one_liner": "EDA on Indian unemployment data using Pandas.",
                "tech_stack": "Python, Pandas, EDA",
                "role": "Solo",
                "is_featured": True
            },
            {
                "title": "Iris Flower Classification",
                "slug": "iris-classification",
                "one_liner": "Random Forest classifier with 93.33% accuracy.",
                "tech_stack": "Python, scikit-learn, ML",
                "role": "Solo",
                "is_featured": True
            }
        ]
        for p_data in projects_data:
            project = Project(**p_data)
            db.session.add(project)

        print("Adding Certifications...")
        certs_data = [
            {
                "title": "The Ultimate Job Ready Data Science Course",
                "issuer": "CodeWithHarry",
                "issue_date": date(2025, 9, 7)
            },
            {
                "title": "Complete 2025 Python Bootcamp",
                "issuer": "CodeWithHarry",
                "issue_date": date(2025, 9, 7)
            }
        ]
        for c_data in certs_data:
            cert = Certification(**c_data)
            db.session.add(cert)

        db.session.commit()
        print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()
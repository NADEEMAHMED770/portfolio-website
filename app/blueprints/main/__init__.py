"""
Main blueprint — public-facing pages.

This blueprint handles the visitor-facing site: home, about, projects,
education, certifications, contact.
"""

from flask import Blueprint

main_bp = Blueprint(
    'main',                # name
    __name__,
    template_folder='templates',
    static_folder='static',
    url_prefix='/'         # mounted at root
)

# Import routes at the bottom to avoid circular imports
from app.blueprints.main import routes  # noqa: E402, F401
from flask import Blueprint

admin_bp = Blueprint(
    'admin', __name__,
    url_prefix='/admin'
)

# Import routes at the bottom to avoid circular imports
from app.blueprints.admin import routes
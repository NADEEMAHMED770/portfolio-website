"""
Entry point for running the Flask development server.

Usage:
    python run.py

Do NOT use this in production — Render runs the app via Gunicorn.
"""

import os
from app import create_app

# Pick config from env var, default to development
config_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_name)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port, debug=True)
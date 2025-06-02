import os

class Config:
    """Configuration class for Flask application."""
    
    # Auth0 credentials
    AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
    API_IDENTIFIER = os.environ.get('API_IDENTIFIER')
    AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
    AUTH0_CLIENT_SECRET = os.environ.get('AUTH0_CLIENT_SECRET')
    
    # Flask settings
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your_secret_key')
    DEBUG = os.environ.get('DEBUG', 'False') == 'True'
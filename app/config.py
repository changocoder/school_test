import os

from dotenv import load_dotenv
load_dotenv()


class ConfigClass:
    """Config class for the application."""
    DEBUG = True
    TESTING = False
    SECRET = os
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
    SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)


class DevelopmentConfig(ConfigClass):
    """Config class for development."""
    DEBUG = True
    TESTING = False


class ProductionConfig(ConfigClass):
    """Config class for production."""
    DEBUG = False
    TESTING = False

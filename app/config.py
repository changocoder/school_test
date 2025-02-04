import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class ConfigClass:
    """Config class for the application."""

    FLASK_DEBUG = os.environ.get("FLASK_DEBUG", int)
    TESTING = False
    SECRET = os.environ.get("SECRET")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET")
    GOOGLE_DISCOVERY_URL = (
        "https://accounts.google.com/.well-known/openid-configuration"
    )
    SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or os.urandom(24)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        hours=int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES"))
    )
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(
        minutes=int(os.environ.get("JWT_REFRESH_TOKEN_EXPIRES"))
    )


class DevelopmentConfig(ConfigClass):
    """Config class for development."""

    FLASK_DEBUG = 1
    TESTING = False


class ProductionConfig(ConfigClass):
    """Config class for production."""

    FLASK_DEBUG = 0
    DEBUG = False
    TESTING = False


class TestConfig(ConfigClass):
    """Config class for testing."""

    FLASK_DEBUG = 1
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_TEST_URI")
    ALEMBIC_INI_PATH = "app/migrations/alembic.ini"

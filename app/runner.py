from flask_login import LoginManager
from oauthlib.oauth2 import WebApplicationClient

from app.app_factory import initialize_app
from app.config import ConfigClass

app = initialize_app(ConfigClass)
# User session management setup
# https://flask-login.readthedocs.io/en/latest
login_manager = LoginManager()
login_manager.init_app(app)
client = WebApplicationClient(ConfigClass.GOOGLE_CLIENT_ID)


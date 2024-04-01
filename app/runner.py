from flask_jwt_extended import JWTManager

from app.app_factory import initialize_app
from app.config import ConfigClass

app = initialize_app(ConfigClass)
jwt = JWTManager(app)

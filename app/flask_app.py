from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.blueprints.exception_handler import handle_api_exception
from app.blueprints.exceptions import APIException

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class, blueprints):
    """Create a new flask application.

    Parameters
    ----------
    config_class : dict
        ConfigClass instance.
    blueprints : list
        List of blueprints to register with the app.

    Returns
    -------
    app
        flask application.
    """
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db, directory="app/migrations")

    app.register_error_handler(APIException, handle_api_exception)

    for bp in blueprints:
        app.register_blueprint(bp)

    return app

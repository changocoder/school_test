from flask import Blueprint
from flask_migrate import Migrate


from app.extension import db
from app.flask_app import create_app
from app.school.blueprints.user.urls import map_urls

user_blueprint = map_urls(Blueprint("user", __name__, url_prefix="/users"))


def initialize_app(config_class):
    """Create a new flask application.

    Parameters
    ----------
    config_class : dict
        ConfigClass instance.

    Returns
    -------
    app
        flask application.
    """
    app = create_app(config_class, [user_blueprint])
    db.init_app(app)

    migrate = Migrate(app, db, directory="app/migrations")

    # app.msg_broker_cxn = connect_to_message_broker(
    #     url=app.config.get("MESSAGE_BROKER_URL")
    # )

    return app

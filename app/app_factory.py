from flask_migrate import Migrate

from app.extension import db
from app.flask_app import create_app


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
    app = create_app(config_class, [])
    db.init_app(app)

    migrate = Migrate(app, db, directory="app/migrations")

    # app.msg_broker_cxn = connect_to_message_broker(
    #     url=app.config.get("MESSAGE_BROKER_URL")
    # )

    return app

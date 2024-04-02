from app.blueprints import api_v1_bp
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
    app = create_app(config_class, [api_v1_bp])

    # app.msg_broker_cxn = connect_to_message_broker(
    #     url=app.config.get("MESSAGE_BROKER_URL")
    # )

    return app

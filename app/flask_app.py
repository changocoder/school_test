from flask import Flask


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

    for bp in blueprints:
        app.register_blueprint(bp)

    return app

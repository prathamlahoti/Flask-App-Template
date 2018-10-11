from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Configuration


db = SQLAlchemy()


def create_app(config_class=Configuration):
    app = Flask(__name__)

    # Setting application configuration
    app.config.from_object(config_class)

    # Associating SQLAlchemy with our application
    db.init_app(app)

    # Importing our blueprints
    from app.errors.handlers import errors
    from app.default_blueprint.routes import default_blueprint

    # Associating our blueprints with application
    app.register_blueprint(errors)
    app.register_blueprint(default_blueprint)
    return app

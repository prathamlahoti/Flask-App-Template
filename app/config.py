import os


class Configuration:
    """ Application configuration options """
    # Keep SECRET_KEY and SQLALCHEMY_DATABASE_URI values in enviroment variables
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
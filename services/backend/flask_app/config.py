import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO= True
    AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
    API_IDENTIFIER = os.getenv("API_IDENTIFIER")
    ALGORITHMS = os.getenv("ALGORITHMS")

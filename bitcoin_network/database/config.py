from os import environ, path
from dotenv import load_dotenv
from sqlalchemy.engine.url import URL

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = URL(
            drivername='postgresql',
            username=environ['PGUSER'],
            password=environ['PGPASSWORD'],
            host=environ['DATABASE_IP'],
            port=environ['DATABASE_PORT']
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

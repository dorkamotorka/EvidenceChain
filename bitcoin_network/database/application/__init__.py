from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()
cors = CORS()

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        # Import blueprints 
        from .api import storage_api_blueprint

        # Register Blueprints
        app.register_blueprint(storage_api_blueprint)

        # Create database
        db.create_all()

        return app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .simple_blockchain import Blockchain

cors = CORS()
blockchain = Blockchain()

def create_app():
    """Create Flask application."""
    app = Flask(__name__)
    app.config.from_object('config.DevConfig')
    cors.init_app(app)

    with app.app_context():
        # Import blueprints 
        from .api import blockchain_api_blueprint

        # Register Blueprints
        app.register_blueprint(blockchain_api_blueprint)

        return app

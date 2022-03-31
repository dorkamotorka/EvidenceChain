from flask import Blueprint
from flask_restful import Api

storage_api_blueprint = Blueprint('storage_api_blueprint', __name__)
storage_api = Api(storage_api_blueprint)

from . import routes

from flask import Blueprint
from flask_restful import Api

blockchain_api_blueprint = Blueprint('blockchain_api_blueprint', __name__)
blockchain_api = Api(blockchain_api_blueprint)

from . import routes

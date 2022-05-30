# Stores file into a database and returns a fuzzy hash of it
import os
import sys
from flask import request, make_response, send_from_directory, jsonify
from flask_restx import Resource, reqparse, abort
from ..models import *
from .. import db
from . import storage_api, storage_api_blueprint
import ssdeep
import random
import time
from werkzeug.utils import secure_filename
from sqlalchemy.exc import IntegrityError

# File directory
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
ALLOWED_EXTENSIONS = {'jpg', 'png', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class HashFile(Resource):
    def __init__(self):
        pass

    def get(self, filename):
        '''
        Input: filename
        Return: Return files hash
        '''
        if filename is None:
            abort(400, "File name is missing")
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file = StorageModel.query.filter_by(filepath=filepath).first()
        if file is None:
            abort(404, "No file exists with that name!")

        return file.get_hash()


class HashFiles(Resource):
    def __init__(self):
        pass

    def get(self):
        '''
        Return all hashes
        '''
        hashes = []
        for hash in StorageModel.query.all():
            hashes.append(hash.to_json())

        return jsonify(hashes)

    def post(self):
        '''
        Store file and return hash
        '''
        if 'file' not in request.files:
            return make_response(jsonify({'message': 'No file part in a request'}), 401)
        f = request.files['file']

        # Check that file has a name, so we can reference it later on
        if f.filename == '':
            return make_response(jsonify({'message': 'No filename in a request'}), 402)

        # Makes sure no malicious actions is taking part
        random.seed(time.time())
        id = random.randint(1, 1000000000000)
        if f and allowed_file(f.filename):
            print(f.filename, file=sys.stderr)
            filename = secure_filename(f.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)
            f.save(path)
            with open(path, "rb") as fr:
                tmp = fr.read()
                #print(tmp, file=sys.stderr)
                hash = ssdeep.hash(tmp)
                print(hash, file=sys.stderr)
                file = StorageModel(
                    id_file = id,
                    filepath = path,
                    fhash = hash,
                )
                try:
                    db.session.add(file)
                    db.session.commit()
                except IntegrityError:
                    abort(400, "File with the same hash already exists!")

                return make_response(jsonify({'message': 'File successfuly uploaded', 'hash': hash}), 200)

        return make_response(jsonify({'message': 'Bad file upload request'}), 404)


storage_api.add_resource(HashFile, "/file/<string:filename>")
storage_api.add_resource(HashFiles, "/files")

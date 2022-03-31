from . import db

class StorageModel(db.Model):
    id_file = db.Column(db.BigInteger, primary_key=True, unique=True)
    filepath = db.Column(db.String(255), nullable=False, unique=True)
    fhash = db.Column(db.String(255), nullable=False, unique=True)

    def get_hash(self):
        return {
            'hash': self.fhash,
        }

    def to_json(self):
        return {
            'id_file': self.id_file,
            'file': self.filepath,
            'hash': self.fhash,
        }

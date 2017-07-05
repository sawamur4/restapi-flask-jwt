from db import db

__author__ = 'junior'


class UserModel(db.Document):
    config_collection_name = 'login'

    id = db.StringField()
    username = db.StringField()
    password = db.StringField()

    def save_to_db(self):
        db.session.save(self)

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter(UserModel.username == username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter(UserModel.id == _id).first()
from ..utils.database import db
from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from passlib.hash import pbkdf2_sha256 as sha256


class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True, index = True)
    created_at = db.Column(db.DateTime(), default = datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default = datetime.utcnow, onupdate = datetime.utcnow)
    first_name = db.Column(db.String(80), nullable = False)
    last_name = db.Column(db.String(80), nullable = False)
    username = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(60),nullable = False, unique= True)
    password_hash = db.Column(db.String(), nullable= False)
    
   # event = db.relationship('Event', backref = 'owner', lazy = True)

    def __init__(self, first_name, last_name, username, email, password_hash):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password_hash = password_hash

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username = username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email = email).first()

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, _hash):
        return sha256.verify(password, _hash)

    def __repr__(self):
        '''String representation of the User class'''
        return f'{self.__class__.__name__} {self.id} {self.__dict__}'


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    username = auto_field()
    email = auto_field()
    first_name = auto_field()
    last_name = auto_field()



    
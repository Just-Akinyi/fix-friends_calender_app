from ..utils.database import db
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from datetime import datetime


class Event(db.Model):


    __tablename__ = 'events'
    id = db.Column(db.Integer(), primary_key = True, index = True)
    created_at = db.Column(db.DateTime(), default = datetime.utcnow)
    updated_at = db.Column(db.DateTime(), default = datetime.utcnow, onupdate = datetime.utcnow)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    location = db.Column(db.String(), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    # user = db.relationship('User',backref = 'events', lazy = True)
    
    def __init__(self, title, description, location, user_id=None):
        self.title = title
        self.description = description
        self.location = location
        self.user_id = user_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def __repr__(self):
        '''String representation of the User class'''
        return f'{self.__class__.__name__} {self.id} {self.__dict__}'

class EventSchema(SQLAlchemySchema):
    class Meta:
        model = Event
        load_instance = True
        sqla_session = db.session

    id = auto_field()
    created_at = auto_field()
    updated_at = auto_field()
    title = auto_field()
    description = auto_field()
    location = auto_field()
    user_id = auto_field()

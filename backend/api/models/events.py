from ..utils.database import db
from datetime import datetime




class Event(db.Model):
    
    
    __tablename__ = 'events'
    id = db.Column(db.Integer(), primary_key = True, index = True)
    title = db.Column(db.String(), nullable = False)
    description = db.Column(db.String(), nullable = False)
    location = db.Column(db.String(), nullable = False)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime(),default = datetime.utcnow)
    updated_at = db.Column(db.DateTime(),onupdate = datetime.utcnow)
    

    
    
    def __repr__(self):
        return f'<Event {self.id}>'

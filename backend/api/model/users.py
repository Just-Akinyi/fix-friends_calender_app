from ..utils.database import db


class User(db.Model):
    
    
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key = True, index = True)
    first_name = db.Column(db.String(50), nullable = False)
    last_name = db.Column(db.String(50), nullable = False)
    username = db.Column(db.String(45), nullable = False, unique = True)
    email = db.Column(db.String(255))
    password_hash = db.Column(db.Text(), nullable= False)
    
    events = db.relationship('Event',backref = 'owner', lazy = True)
    
    def __repr__(self):
        return f'<User {self.username}>'
from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User 
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus




auth_namespace = Namespace('auth', description ='Namespace for Authentication' )



signup_model = auth_namespace.model(
    
    'signup', {
        'id':fields.Integer(),
        'firstname':fields.String(required = True, description = 'Firstname'),
        'lastname':fields.String(required = True, description = 'Lastname'),
        'username':fields.String(required = True, description = 'Username'),
        'email':fields.String(required = True, description = 'An email'),
        'password': fields.String(required = True, description = 'Password')
    }
    
)
user_model = auth_namespace.model(
    
    'user', {
        'id':fields.Integer(),
        'firstname':fields.String(required = True, description = 'Firstname'),
        'lastname':fields.String(required = True, description = 'Lastname'),
        'username':fields.String(required = True, description = 'Username'),
        'email':fields.String(required = True, description = 'An email'),
        'password': fields.String(required = True, description = 'Password'),
        'created_at':fields.DateTime()
    }
    
)



@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(signup_model)
    def post(self):
        '''
        Create a new user account
        
        '''
        data = request.get_json()
        
        new_user = User(
            first_name= data.get('firstname'),
            last_name= data.get('lastname'),
            username = data.get('username'),
            email = data.get('email'),
            password_hash = generate_password_hash(data.get('password'))
        )
        
        new_user.save()
        return new_user, HTTPStatus.CREATED 
    
    
    
    
      

    
@auth_namespace.route('/login')
class Login(Resource):
    
    
    def post(self):
        '''
        Generate a JWT pair
        '''
        pass
    
    


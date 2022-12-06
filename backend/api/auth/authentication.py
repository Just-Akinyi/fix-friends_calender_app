from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User 
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)
from werkzeug.exceptions import Conflict, BadRequest




auth_namespace = Namespace('auth', description ='Namespace for Authentication' )


signup_model = auth_namespace.model(
    
    'signup', {
        'id':fields.Integer(),
        'firstname':fields.String(required = True, description = 'Firstname'),
        'lastname':fields.String(required = True, description = 'Lastname'),
        'username':fields.String(required = True, description = 'Username'),
        'email':fields.String(required = True, description = ' An email'),
        'password_hash':fields.String(required = True, description = 'Password')
    }
    
)
user_model = auth_namespace.model(
    
    'user', {
        'id':fields.Integer(),
        'first_name':fields.String(required = True, description = 'Firstname'),
        'last_name':fields.String(required = True, description = 'Lastname'),
        'username':fields.String(required = True, description = 'Username'),
        'email':fields.String(required = True, description = 'An email'),
        'password_hash':fields.String(required = True, description = 'Password'),
        'created_at':fields.DateTime()
    }
    
)

login_model = auth_namespace.model(
    'login',{
        'email':fields.String(required = True, description = 'An email'),
        'password_hash':fields.String(required = True, description = 'Password')
    }
    
)



@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(user_model)
    
    def post(self):
        '''
        Create a new user account
        
        '''
        data = request.get_json()
        
        try:
        
            new_user = User(
                first_name= data.get('firstname'),
                last_name= data.get('lastname'),
                username = data.get('username'),
                email = data.get('email'),
                password_hash = generate_password_hash(data.get('password_hash'))
            )
            
            new_user.save()
            return new_user, HTTPStatus.CREATED 
        except Exception as e:
            raise Conflict(f'User with email {data.get("email")} exist')
    

    
@auth_namespace.route('/login')
class Login(Resource):
    
    @auth_namespace.expect(login_model)
   # @auth_namespace.marshal_with(login_model)
    def post(self):
        '''
        Generate a JWT pair
        '''
        data = request.get_json()
     
            
        email = data.get('email')
        password= data.get('password_hash')
            
        user = User.find_by_email(email)
        if (user is not None)and check_password_hash(user.password_hash, password):
                access_token = create_access_token(identity = user.username)
                refresh_token = create_refresh_token(identity = user.username)
                
                response = {
                'access_token':access_token,
                'refresh_token':refresh_token
                }
                
                return response, HTTPStatus.OK   
    
        raise BadRequest("Invalid username or password")
        
            
@auth_namespace.route('/refresh')
class Refresh(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        
       username = get_jwt_identity()
       access_token = create_access_token(identity = username)
       
       return {'access_token':access_token}, HTTPStatus.OK
   


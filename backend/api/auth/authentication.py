from flask_restx import Namespace, Resource, fields
from flask import request
from ..models.users import User 
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus
from flask_jwt_extended import (create_access_token, create_refresh_token, jwt_required, get_jwt_identity)




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

email_model = auth_namespace.model(
   'email',{
    'email': fields.Sring(required =True, description = 'validate email')
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
        
        new_user = User(
            firstname= data.get('firstname'),
            username = data.get('username'),
            email = data.get('email'),
            password_hash = generate_password_hash(data.get('password_hash'))
        )
        
        new_user.save()
        return new_user, HTTPStatus.CREATED 
    
        
        
        
    
    
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
        
        user = User.query.filter_by(email=email).first()
        
        if (user is not None)and check_password_hash(user.password_hash, password):
            access_token = create_access_token(identity = user.username)
            refresh_token = create_refresh_token(identity = user.username)
            
            response = {
            'access_token':access_token,
            'refresh_token':refresh_token
            }
            
            return response, HTTPStatus.OK    
        
@auth_namespace.route('/refresh')
class Refresh(Resource):
    
    @jwt_required(refresh=True)
    def post(self):
        
       username = get_jwt_identity()
       access_token = create_access_token(identity = username)
       
       return {'access_token':access_token}, HTTPStatus.OK
    
@auth_namespace.route('/forgot-password')
class ForgotPassword:
    @auth_namespace.expect(email_model)
    def post(self):
        data = requests.get_json()
        get_email = data['email']
        user = User.query.filter_by(email=get_email).first()

        if user: 
            send_reset_mail(user.email)
            return f"password reset has been sent to {get_email}", HTTPStatus.OK    
    
        return f"email {get_email} does not exist in our database", HTTPStatus.NOT_FOUND
@auth_namespace.route('/reset-password')
class ResetPassword:
    @auth_namespace.expect(password_model)
    def patch(self, email):
        pass 
        
        
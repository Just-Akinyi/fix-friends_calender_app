from flask_restx import Namespace, Resource



auth_namespace = Namespace('auth', description ='Namespace for Authentication' )


@auth_namespace.route('/signup')
class SignUp(Resource):
    
    def post(self):
        '''
        Create a new user account
        '''
        pass
    
    
@auth_namespace.route('/login')
class Login(Resource):
    
    def post(self):
        '''
        Generate a JWT pair
        '''
        pass
    
    
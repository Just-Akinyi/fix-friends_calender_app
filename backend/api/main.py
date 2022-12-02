from flask import Flask
from flask_restx import Api
from .auth.authentication import auth_namespace
from .event.event import event_namespace





def create_app():
    app = Flask(__name__)
    
    api = Api(app)
    api.add_namespace(auth_namespace)
    api.add_namespace(event_namespace)
    
    return app
    
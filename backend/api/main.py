from flask import Flask
from flask_restx import Api
from .auth.authentication import auth_namespace
from .event.event import event_namespace
from .config.config import config_dict
from .utils.database import db
from .models.events import Event
from .models.users import User
from flask_migrate import Migrate




def create_app(config = config_dict['dev']):
    app = Flask(__name__)
    app.config.from_object(config) 
    db.init_app(app)
    migrate = Migrate(app, db)
    
    api = Api(app)
    api.add_namespace(auth_namespace)
    api.add_namespace(event_namespace)
    
    @app.shell_context_processor  
    def make_shell_context():
            return{
                'db':db,
                'User':User,
                'Event':Event
            }
    
    return app
    
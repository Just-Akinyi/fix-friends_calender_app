import os
from decouple import config


BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class Config:
    SECRET_KEY = config('SECRET_KEY', 'secret')
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    
    
class DevConfig(Config):
    DEBUG = config('DEBUG', cast = bool)
    SQLALCHEMY_ECHO=True
  
    
class TestConfig(Config):
    pass

class ProdConfig(Config):
    pass 

config_dict = {
    'dev':DevConfig,
    'prod':ProdConfig,
    'test':TestConfig
}
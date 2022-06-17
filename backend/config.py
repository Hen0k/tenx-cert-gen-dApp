import os
from uuid import uuid4
from dotenv import load_dotenv
from datetime import timedelta


load_dotenv()

def get_uuid():
    return uuid4().hex

class ApplicationConfig(object):
    """ Flask application config """
    JWT_SECRET_KEY = get_uuid()
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    # SECRET_KEY = os.urandom(20).hex()

    # Flask-MongoEngine settings
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_ENDPOINT')
    }

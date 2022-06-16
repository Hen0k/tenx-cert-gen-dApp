import os
from dotenv import load_dotenv


load_dotenv()


class Config(object):
    """ Flask application config """
    # SECRET_KEY = os.urandom(20).hex()

    # Flask-MongoEngine settings
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_ENDPOINT')
    }

"""Initialize Flask app."""
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_app.routes import init_routes


db = MongoEngine()


def init_app():
    """Construct core Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    
    app = init_routes(app)
    

    # with app.app_context():
        # from . import routes
    return app

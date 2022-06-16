"""Routes for parent Flask app."""
from flask import render_template, render_template_string
# from flask import current_app as app

def init_routes(app):
    """A factory function that takes in the server 
    object and initializes the routes.
    """
    @app.route("/test")
    def test():
        return "Hello, world"
        
    @app.route('/auth')
    def authenticate():
        pass

    return app
from flask import Flask # importing flask
from app.extensions import db, migrate
from config import Config

# Creating an apppliction factory function

def create_app():
    app = Flask(__name__) # creating an instance
    app.config.from_object('config.Config')

    
    db.init_app(app)
    migrate.init_app(app, db)
    
    @app.route('/') # index route
    def index():
        return 'Hello'
    
    
    
    return app # returning the app instance
    
    
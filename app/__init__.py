from flask import Flask # importing flask

# Creating an apppliction factory function

def create_app():
    app = Flask(__name__) # creating an instance
    
    @app.route('/') # index route
    def index():
        return 'Hello'
    
    
    
    return app # returning the app instance
    
    
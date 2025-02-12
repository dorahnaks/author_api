from flask import Flask # importing flask

app = Flask(__name__) # creating an instance

@app.route('/') 
def author_api():
    return '<h1>Author API</h1>' 

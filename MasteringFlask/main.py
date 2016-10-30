"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    return "Hello Python Flask World!"


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


if __name__ == '__main__':
    #import os
    #HOST = os.environ.get('SERVER_HOST', 'localhost')
    #try:
    #    PORT = int(os.environ.get('SERVER_PORT', '5555'))
    #except ValueError:
    #    PORT = 5555
    #app.run(HOST, PORT)
    #the following will run at http://localhost:5000
    app.run()

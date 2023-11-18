# server.py

"""
This module defines the server configuration required to run the app
successfully.

# Configuration defined
Server as Flask APP
Flask Blueprint
Flask SQLAlchemy for DB
Flask Migrate for DB-ORM
CSRF Protection
Error Handling
"""

# imports


import config
import routes
from flask import Blueprint, Flask
from flask_cors import CORS
from flask_migrate import Migrate
from forms import csrf
from models import db

# configurations

server = Flask(__name__)

server.config['SECRET_KEY'] = config.secretKey

server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_MODIFICATIONS_TRACKS'] = config.SQLALCHEMY_MODIFICATIONS_TRACKS  # noqa

db.init_app(server)
db.app = (server)
migrate = Migrate(server, db)
WTF_CSRF_SECRET_KEY = config.secretKey
csrf.init_app(server)

cors = CORS(server, resources={
            r"/*": {"origins": "http://127.0.0.1:5000"}})

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(blueprint)

# application run
if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run()

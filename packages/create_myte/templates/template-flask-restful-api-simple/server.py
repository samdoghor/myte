# app.py

"""
This module defines...
"""

# imports

from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api

import config
from models import db
from resources import Index, Todo, TodoItem, User

# configurations

server = Flask(__name__)

server.debug = config.DEBUG
server.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
server.config['SECRET_KEY'] = config.SECRET_KEY

db.init_app(server)
db.server = server
migrate = Migrate(server, db)
api = Api(server)

# routes

api.add_resource(Index, '/')
api.add_resource(Todo, '/todo/', '/todo/<string:id>/')
api.add_resource(TodoItem, '/todo_item/', '/todo_item/<string:id>/')
api.add_resource(User, '/user/', '/user/<string:id>/')

# entrypoint


if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run()

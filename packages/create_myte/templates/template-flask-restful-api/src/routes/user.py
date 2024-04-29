# user.py
"""
The module defines ....
"""

# imports

from flask import Blueprint
from resources import User

# configuration

UserBlueprint = Blueprint("user", __name__)

# routes

UserBlueprint.route(
    "/users", methods=['POST'])(User.create)

UserBlueprint.route(
    "/users", methods=['GET'])(User.view_all)

UserBlueprint.route(
    "/users/<int:id>", methods=['GET'])(User.view_one)

UserBlueprint.route(
    "/users/<int:id>", methods=['PUT'])(User.update)

UserBlueprint.route(
    "/users/<int:id>", methods=['DELETE'])(User.delete)

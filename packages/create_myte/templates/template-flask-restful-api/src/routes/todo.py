# todo.py
"""
The module defines ....
"""

# imports

from flask import Blueprint
from resources import Todo

# configuration

TodoBlueprint = Blueprint("todo", __name__)

# routes

TodoBlueprint.route(
    "/todos", methods=['POST'])(Todo.create)

TodoBlueprint.route(
    "/todos", methods=['GET'])(Todo.view_all)

TodoBlueprint.route(
    "/todos/<int:id>", methods=['GET'])(Todo.view_one)

TodoBlueprint.route(
    "/todos/<int:id>", methods=['PUT'])(Todo.update)

TodoBlueprint.route(
    "/todos/<int:id>", methods=['DELETE'])(Todo.delete)

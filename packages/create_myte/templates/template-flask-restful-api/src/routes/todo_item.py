# todo_item.py
"""
The module defines ....
"""

# imports

from flask import Blueprint
from resources import TodoItem

# configuration

TodoItemBlueprint = Blueprint("todo_item", __name__)

# routes

TodoItemBlueprint.route(
    "/todo_items", methods=['POST'])(TodoItem.create)

TodoItemBlueprint.route(
    "/todo_items", methods=['GET'])(TodoItem.view_all)

TodoItemBlueprint.route(
    "/todo_items/<int:id>", methods=['GET'])(TodoItem.view_one)

TodoItemBlueprint.route(
    "/todo_items/<int:id>", methods=['PUT'])(TodoItem.update)

TodoItemBlueprint.route(
    "/todo_items/<int:id>", methods=['DELETE'])(TodoItem.delete)

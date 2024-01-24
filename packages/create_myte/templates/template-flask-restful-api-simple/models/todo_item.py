# todo_item.py

"""
The model ...
"""

# imports

from datetime import datetime

from . import db

# pylint: disable=R0903


class TodoItem(db.Model):

    """
    todo item model class representing ....
    """

    __tablename__ = "todo_items"

    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    status = db.Column(db.Boolean(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    todo_id = db.Column(db.Integer, db.ForeignKey(
        'todos.id'), nullable=False)

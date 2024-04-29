# todo.py

"""
The model ...
"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db

# pylint: disable=R0903


class Todo(db.Model):

    """
    todo model class representing ....
    """

    __tablename__ = "todos"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    title = db.Column(db.String(), nullable=False)
    description = db.Column(db.String(), nullable=True)
    status = db.Column(db.Boolean(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'users.id'), nullable=False)

    # relationships

    todo_item = db.relationship("TodoItem", backref="todos", lazy=True)

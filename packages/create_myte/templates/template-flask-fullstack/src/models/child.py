"""
The model represents a user entity with attributes such as name,
address,contact information, and registration details, associated with contact
persons and jobs.
"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID

from . import db
from .abc import BaseModel, MetaBaseModel

# pylint: disable=R0903


class Children(db.Model, BaseModel, metaclass=MetaBaseModel):

    """
    user model class representing the 'children' table in the database.
    """

    __tablename__ = "children"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    full_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=False)
    phone_number = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True)

    # foreign keys

    parent_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'parents.id'), nullable=False)

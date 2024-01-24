"""
The model represents a user entity with attributes such as name,
address,contact information, and registration details, associated with contact
persons and jobs.
"""

# imports

from datetime import datetime

from . import db
from .abc import BaseModel, MetaBaseModel

# pylint: disable=R0903


class User(db.Model, BaseModel, metaclass=MetaBaseModel):

    """
    user model class representing the 'users' table in the database.
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=True)
    phone_number = db.Column(db.String(), unique=True, nullable=True)
    street_name = db.Column(db.String(), nullable=False)
    city = db.Column(db.String(), nullable=False)
    state = db.Column(db.String(), nullable=False)
    country = db.Column(db.String(), nullable=False)
    zipcode = db.Column(db.Integer(), nullable=False)
    user_photo = db.Column(db.String(), nullable=True)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow,
        nullable=True
    )

    # relationships

    siblings = db.relationship(
        "Sibling", backref="users", lazy=True)

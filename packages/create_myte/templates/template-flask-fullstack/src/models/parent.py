"""
The model represents a user entity with attributes such as name,
address,contact information, and registration details, associated with contact
persons and jobs.
"""

# imports

from datetime import datetime
from uuid import uuid4

from sqlalchemy import UUID
from werkzeug.security import check_password_hash, generate_password_hash

from . import db
from .abc import BaseModel, MetaBaseModel

# pylint: disable=R0903


class Parent(db.Model, BaseModel, metaclass=MetaBaseModel):

    """
    user model class representing the 'parents' table in the database.
    """

    __tablename__ = "parents"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    phone_number = db.Column(db.String(), unique=True, nullable=False)
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

    # this generates an encrypted password for the password you entered

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # this decode the encrypted password for the password you entered

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # relationships

    children = db.relationship(
        "Children", backref="parents", lazy=True)

# models.py

"""
This module defines...
"""

# imports

from datetime import datetime
from uuid import uuid4

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UUID
from werkzeug.security import check_password_hash, generate_password_hash

# configurations

db = SQLAlchemy()

# models


class Parent(db.Model):
    ''' Defines the model for parent details '''

    __tablename__ = 'parents'

    # uuid was used for better user id encryption

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)

    first_name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)
    email_address = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True,
                           onupdate=datetime.utcnow)

    # this generates an encrypted password for the password you entered

    def set_password(self, password):
        self.password = generate_password_hash(password)

    # this decode the encrypted password for the password you entered

    def check_password(self, password):
        return check_password_hash(self.password, password)

    # relationships
    child = db.relationship("Child", backref="parents", lazy=True)


class Child(db.Model):
    ''' Defines the model for child details'''

    __tablename__ = 'children'

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    first_name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True,
                           onupdate=datetime.utcnow)

    # foreign keys
    parent_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        "parents.id"), nullable=False)

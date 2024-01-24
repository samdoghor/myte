# models.py

"""
This module defines...
"""

# imports

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

# configurations

db = SQLAlchemy()

# models


class Parent(db.Model):
    ''' Defines the model for parent details'''

    __tablename__ = 'parents'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True,
                           onupdate=datetime.utcnow)

    # relationships
    child = db.relationship("Child", backref="parents", lazy=True)


class Child(db.Model):
    ''' Defines the model for child details'''

    __tablename__ = 'children'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
    middle_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=False)

    created_at = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_at = db.Column(db.DateTime(), nullable=True,
                           onupdate=datetime.utcnow)

    # foreign keys
    parent_id = db.Column(db.Integer, db.ForeignKey(
        "parents.id"), nullable=False)

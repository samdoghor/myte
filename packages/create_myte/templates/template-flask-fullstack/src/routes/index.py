# index.py

"""
This defines the routes for Homepage
"""

from flask import Blueprint

from resources import IndexResource

index_blueprint = Blueprint("index", __name__)

index_blueprint.route("/")(IndexResource.index)

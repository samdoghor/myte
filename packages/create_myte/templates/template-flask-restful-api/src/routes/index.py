# index.py
"""
The module defines ....
"""

# imports

from flask import Blueprint
from resources import Index

# configuration

IndexBlueprint = Blueprint("index", __name__)

# routes

IndexBlueprint.route("/index", methods=['GET'])(Index.status_200)
IndexBlueprint.route("/", methods=['GET'])(Index.home)

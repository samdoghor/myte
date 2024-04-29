# index.py
"""
The module defines ....
"""

from flask import jsonify
from flask_restful import Resource


class Index(Resource):
    """ This class defines... """

    @staticmethod
    def status_200():
        """  """
        return jsonify({
            "Message": "Welcome to Myte API",
            "Status Code": 200,
        }), 200

    @staticmethod
    def home():
        """  """
        return jsonify({
            "Message": "Welcome to Myte API",
            "Status Code": 200,
        }), 200

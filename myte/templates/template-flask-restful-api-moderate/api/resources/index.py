# index.py
"""
The module defines ....
"""

from flask_restful import Resource


class Index(Resource):
    """ This class defines... """

    def get(self):
        """ This function defines... """

        return {'hello': 'world'}

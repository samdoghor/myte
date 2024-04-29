# index.py

"""
This module defines the resource for the index page
"""


from flask import render_template

# pylint: disable=R0903


class IndexResource:

    """ Index Resources """

    # pylint: disable=E0211

    def index():
        """ Confirms and displays basic info that the server is running """

        pass

        return render_template('pages/index/index.html'), 200

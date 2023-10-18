# app.py

"""
This module defines...
"""

# imports

from flask import Flask, render_template
from flask_migrate import Migrate

import config
from models import db

# configurations

app = Flask(__name__)

app.debug = config.DEBUG
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
app.config['SECRET_KEY'] = config.SECRET_KEY

db.init_app(app)
db.app = app
migrate = Migrate(app, db)

# application


@app.route('/', methods=['GET'])
def index():
    """ This function defines... """

    # write your logic here

    return render_template('pages/index.html'), 200

# entrypoint


if __name__ == "__main__":
    app.debug = config.DEBUG
    app.run()

#  server.py

"""
## Module Name: server.py

This module is responsible for ...

It imports necessary modules, configures the server, and defines routes and
endpoints for the API.

"""

# imports

import config
import routes
from flasgger import Swagger
from flask import Blueprint, Flask
from flask_migrate import Migrate
from flask_restful import Api
from models import db

# instantiation/configuration

server = Flask(__name__)
server.config['SECRET_KEY'] = config.SECRET_KEY

server.config["SWAGGER"] = {
    "swagger_version": "2.0",  # noqa : only modified to suit swagger_version of choice
    "title": "",   # put the title here (APP Name)

    "description": """ """,

    "termsOfService": "#",  # put your terms of service here
    "version": "1.0.0",  # version of your API
    "uiversion": 3,  # noqa : only modified to suit swagger UI version of choice
    "static_url_path": "/v1/docs",
}
swagger_config = Swagger.DEFAULT_CONFIG.copy()
swagger_config["openapi"] = "3.0.3"  # noqa : only modified to suit openapi version of choice
Swagger(server, config=swagger_config)

server.debug = config.DEBUG
server.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS  # noqa
db.init_app(server)
db.app = server
migrate = Migrate(server, db)
api = Api(server)

for blueprint in vars(routes).values():
    if isinstance(blueprint, Blueprint):
        server.register_blueprint(
            blueprint, url_prefix=config.APPLICATION_ROOT)

# error handling


# run


if __name__ == "__main__":
    server.debug = config.DEBUG
    server.run(host=config.HOST, port=config.PORT)

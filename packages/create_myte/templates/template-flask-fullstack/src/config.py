# config.py

"""
This module define all important variables, connection to DB
"""

# imports

import os

from dotenv import load_dotenv

# configurations

load_dotenv()

DATABASE_HOST = os.getenv('DATABASE_HOST')
DATABASE_PORT = os.getenv('DATABASE_PORT')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
DATABASE_NAME = os.getenv('DATABASE_NAME')

DEBUG = True

# databases
# delete any database you don't want to use

# postgreSQL - default (pip install psycopg2 (windows users) or psycopg2-binary (linux and mac users))  # noqa

SQLALCHEMY_DATABASE_URI = f'postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'  # noqa

# # mySQL (pip install mysql-connector-python)
# uncomment line 35 to use MySQL DB and comment line 30

# SQLALCHEMY_DATABASE_URI = f'mysql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}'  # noqa

# # SQLite (goto https://www.sqlite.org/download.html, download and install, if you've not)  # noqa
# uncomment line 40 to use SQLite DB and comment line 30

# SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_NAME}.db'

SQLALCHEMY_MODIFICATIONS_TRACKS = False

appHost = os.getenv('APPHOST')
appPort = os.getenv('APPPORT')

environment = os.getenv('ENVIRONMENT')

secretKey = os.getenv('SECRETKEY')

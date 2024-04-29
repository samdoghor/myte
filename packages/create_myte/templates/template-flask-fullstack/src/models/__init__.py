# imports
from flask_sqlalchemy import SQLAlchemy

# configurations
db = SQLAlchemy()

# module imports
from .parent import Parent
from .child import Children

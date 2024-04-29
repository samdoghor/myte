# imports
from flask_sqlalchemy import SQLAlchemy

# configurations
db = SQLAlchemy()

from .todo import Todo
from .todo_item import TodoItem
from .user import User
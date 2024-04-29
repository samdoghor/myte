from flask_wtf.csrf import CSRFProtect

from .user import CreateUserForm, DeleteUserForm

csrf = CSRFProtect()

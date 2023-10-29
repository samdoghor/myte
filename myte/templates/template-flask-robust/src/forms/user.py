"""
This module defines all forms needed by the users
"""
# imports

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import IntegerField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


# forms


class CreateUserForm(FlaskForm):

    """ This class is use to create new users """

    name = StringField('Name', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[Email()])
    phone_number = IntegerField('Phone Number')
    street_name = StringField('Street Name', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = SelectField('Country', validators=[DataRequired()], choices=[])
    zipcode = StringField('Zipcode', validators=[DataRequired()])
    user_photo = FileField('Logo', validators=[FileAllowed(
        ['jpg', 'png'], 'JPG & PNG Formats Only!')])
    create_user = SubmitField('Add user')


class DeleteUserForm(FlaskForm):

    """ This class is use to create new users """

    delete_user = SubmitField('Yes')

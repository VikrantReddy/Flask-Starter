from flask_wtf import FlaskForm
from wtforms import PasswordField, TextField
from wtforms.validators import Email, EqualTo, Required


class LoginForm(FlaskForm):
    email = TextField('Email Address', [Email(),
                                        Required(message='Forgot your email address?')])
    password = PasswordField('Password', [
        Required(message='Must provide a password. ;-)')])

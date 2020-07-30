from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    userid = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])

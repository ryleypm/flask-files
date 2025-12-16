from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    username = StringField("Username", validators=[DataRequired(), Length(min = 5, max = 20)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min = 8)])
    confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password")])

class signInForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
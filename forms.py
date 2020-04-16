from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=100)])
	confirmPassword = PasswordField("Confirm Password", validators=[DataRequired(), Length(min=5, max=100), EqualTo("password")])

	submit = SubmitField("Done")

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired(), Length(min=2, max=15)])
	password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=100)])

	submit = SubmitField("Login")

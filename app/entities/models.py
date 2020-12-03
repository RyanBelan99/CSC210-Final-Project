
from wtforms import SubmitField, StringField, PasswordField, validators
from flask_wtf import FlaskForm 


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')




class SignupForm(FlaskForm):
    name = StringField('Name')
    username = StringField('Enter a Username', [validators.DataRequired()])
    password = PasswordField('Enter a Password', [validators.DataRequired(), validators.Length(min=4, max=62)])
    submit = SubmitField('Signup')




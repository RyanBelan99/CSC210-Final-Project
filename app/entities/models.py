
from wtforms import SubmitField, StringField, PasswordField, IntegerField Birthday validators
from flask_wtf import FlaskForm 


class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = StringField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')




class SignupForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    bith = DateField("Enter your Birthday", [validators.DataRequired()])
    age = IntegerField("Age", [validators.DataRequired()])
    username = StringField('Enter a Username', [validators.DataRequired()])
    password = PasswordField('Enter a Password', [validators.DataRequired(), validators.Length(min=4, max=62)])
    submit = SubmitField('Signup')




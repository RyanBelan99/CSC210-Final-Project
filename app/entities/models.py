from wtforms import TextAreaField, SubmitField, StringField, PasswordField, IntegerField, DateField, FieldList, validators
from flask_wtf import FlaskForm

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    birth = StringField("Enter your Birthday", [validators.DataRequired()])
    username = StringField('Enter a Username', [validators.DataRequired()])
    password = PasswordField('Enter a Password', [validators.DataRequired(), validators.Length(min=4, max=62)])
    submit = SubmitField('Sign Up')

class PostForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    ingredients = FieldList(StringField('ingredient'), min_entries=10, max_entries=10)
    instructions = FieldList(StringField('instructions'), min_entries=10, max_entries=10)
    submit = SubmitField('Post')

class LikeForm(FlaskForm):
    submit = SubmitField('Like')

class EditProfileForm(FlaskForm):
    name = StringField('Name', [validators.DataRequired()])
    birth = StringField("Enter your Birthday", [validators.DataRequired()])
    submit = SubmitField('Submit')

class ChangePasswordForm(FlaskForm):
    curPassword = PasswordField('Current Password', [validators.DataRequired()])
    newPassword = PasswordField('New Password', [validators.DataRequired()])
    submit = SubmitField('Submit')

class EditRecipeForm(FlaskForm):
    title = StringField('title', [validators.DataRequired()])
    newIngredients = FieldList(StringField('ingredient'), min_entries=10, max_entries=10)
    newInstructions = FieldList(StringField('instructions'), min_entries=10, max_entries=10)
    submit = SubmitField('Submit')
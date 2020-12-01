# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.app import db
from app.mod_auth.forms import LoginForm
from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)
# Set the route and accepted methods

@mod_auth.route('/login')
def signin():
    return render_template("login.html")

@mod_auth.route('/login', method=['POST'])
def login_post():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):

    #         session['user_id'] = user.id

    #         flash('Welcome %s' % user.name)

    #         return redirect(url_for('auth.home'))

    #     flash('Wrong email or password', 'error-message')

    #return render_template("login.html")

@mod_auth.route('/signup', method=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    return redirect(url_for('auth.login'))


@mod_auth.route('/logout')    
def logout():
    return redirect(url_for('index.html')) 


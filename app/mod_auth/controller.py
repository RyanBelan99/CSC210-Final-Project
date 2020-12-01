# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.app import db
from app.entities.models import LoginForm
#from app.mod_auth.models import User

# Define the blueprint: 'auth', set its url prefix: app.url/auth
mod_auth = Blueprint('auth', __name__)

# Set the route and accepted methods
@mod_auth.route('/login')
def signin():
    return render_template("login.html")

@mod_auth.route('/login', methods=['POST'])
def login_post():

    return render_template("login.html")

@mod_auth.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    return redirect(url_for('auth.login'))


@mod_auth.route('/logout')    
def logout():
    return redirect(url_for('mod_main.index.html')) 

@mod_auth.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@mod_auth.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500    


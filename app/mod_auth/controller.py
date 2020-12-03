from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.entities.models import LoginForm

mod_auth = Blueprint('auth', __name__, url_prefix='/mod_auth')

@mod_auth.route('/login')
def login():
    return render_template("auth/login.html")

@mod_auth.route('/login', methods=['POST'])
def login_post():
    return render_template("auth/login.html")

@mod_auth.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    return redirect(url_for('mod_auth.login'))


@mod_auth.route('auth/logout')    
def logout():
    return redirect(url_for('mod_main.index.html')) 



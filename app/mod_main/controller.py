# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db

mod_main = Blueprint('mod_main', __name__)

@mod_main.route('/')
def index():
        return render_template("index.html")

@mod_main.route('/login')
def login():
        return redirect(url_for('mod_auth.login'))

# @mod_main.route('/createPost')
# def postLogin():
#         return redirect(url_for('mod_auth.login'))

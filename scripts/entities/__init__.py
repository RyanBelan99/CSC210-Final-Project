from Flask import flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'veryverysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
auth = 
main = 
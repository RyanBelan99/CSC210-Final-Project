from Flask import flask
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def create_app(config_name):
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'veryverysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    



    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/main')
    
    return app
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Blueprint
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    application = app
    
    app.config['SECRET_KEY'] = 'veryverysecretkey'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from app.entities.users import User   

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))  


    from .mod_auth.controller import mod_auth as auth_module
    app.register_blueprint(auth_module)

    from .mod_main.controller import mod_main as main_module
    app.register_blueprint(main_module)

    return app    



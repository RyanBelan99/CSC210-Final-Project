from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_login import current_user
from app.config import Config

if __name__ == "__main__":
     app.run(ssl_context=('cert.pem', 'key.pem'))

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    bootstrap = Bootstrap(app)
    application = app

    migrate = Migrate(app,db)
    db.init_app(app)

    if not scheduler.running:
        scheduler.init_app(app)
        scheduler.start()

    login_manager = LoginManager()
    login_manager.login_view = 'mod_main.index'
    login_manager.init_app(app)

    from app.dbschema.users import User
    from app.dbschema.recipe import Recipe
    from app.dbschema.likes import LikePost

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500

    @app.context_processor
    def inject_user():
        username = birth = name = None
        if current_user.is_authenticated:
            name = current_user.name
            birth = current_user.birth
            username = current_user.username
        return dict(username=username, birth=birth, name=name)


    from .mod_auth.controller import mod_auth as auth_module
    app.register_blueprint(auth_module)

    from .mod_main.controller import mod_main as main_module
    app.register_blueprint(main_module)

    from .mod_post.controller import mod_post as post_module
    app.register_blueprint(post_module)

    from .mod_user.controller import mod_user as user_module
    app.register_blueprint(user_module)

    return app

from app.tasks import scheduler

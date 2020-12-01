from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate


app = Flask(__name__)
application = app
app.config['SECRET_KEY'] = 'assignment10'

bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///list.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app,db)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/', methods = ['POST', 'GET'])
def index():
	return render_template("index.html")

# Import a module / component using its blueprint handler variable (mod_auth)
from app.mod_auth.controller import mod_auth as auth_module

# Register blueprint(s)
app.register_blueprint(auth_module)

if __name__ == "__main__":
    app.run(debug=True)

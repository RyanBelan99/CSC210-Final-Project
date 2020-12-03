from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from app import db, app

migrate = Migrate(app,db)

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

 


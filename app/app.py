from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from app import db, app

migrate = Migrate(app,db)


 


# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.dbschema.recipe import Recipe, CompetingRecipes
from sqlalchemy import desc
from app import db

mod_main = Blueprint('mod_main', __name__)

@mod_main.route('/')
def index():
    competing_ids = CompetingRecipes.query.all()
    recipes=[]
    for c in competing_ids:
        recipes.append(Recipe.query.filter_by(id=c.id).first_or_404())
    return render_template("index.html", recipes=recipes)

@mod_main.route('/login')
def login():
        return redirect(url_for('mod_auth.login'))

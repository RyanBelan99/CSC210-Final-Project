# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.dbschema.recipe import Recipe, CompetingRecipes
from sqlalchemy import desc
from app import db

mod_main = Blueprint('mod_main', __name__)

@mod_main.route('/')
def index():
    recipes = db.session.query(Recipe, CompetingRecipes).order_by(desc(Recipe.total_likes))
    usernames=[]
    for recipe in recipes:
        usernames.append(Recipe.query.filter_by(id=recipe.id).first_or_404().username)
    return render_template("index.html", recipes=recipes, usernames=usernames)

@mod_main.route('/login')
def login():
        return redirect(url_for('mod_auth.login'))

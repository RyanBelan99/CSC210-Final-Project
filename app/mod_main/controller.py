# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.dbschema.recipe import Recipe, CompetingRecipes
from app.dbschema.weeklyWipe import LastWeeksWinners
from sqlalchemy import desc
from app import db

mod_main = Blueprint('mod_main', __name__)

@mod_main.route('/')
def index():
    recipes = Recipe.query.order_by(desc(Recipe.total_likes)).limit(5)
    winnerRecipes = db.session.query(LastWeeksWinners).limit(3)
    return render_template("index.html", recipes=recipes, winnerRecipes = winnerRecipes)

@mod_main.route('/login')
def login():
        return redirect(url_for('mod_auth.login'))

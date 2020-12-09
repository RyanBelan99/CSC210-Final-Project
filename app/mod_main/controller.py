# Import flask dependencies
from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app.dbschema.recipe import Recipe, CompetingRecipes
from app.dbschema.weeklyWipe import LastWeeksWinners, WeekInfo
from sqlalchemy import desc
from app import db
from app.tasks import initFirstWeek

mod_main = Blueprint('mod_main', __name__)

@mod_main.route('/')
def index():
    competing_ids = CompetingRecipes.query.all()
    recipes=[]
    for c in competing_ids:
        recipes.append(Recipe.query.filter_by(id=c.id).first_or_404())
    recipes.sort(key=lambda x: x.total_likes, reverse=True)
    winnerRecipes = LastWeeksWinners.query.limit(3)
    if db.session.query(WeekInfo).count() == 0:
            initFirstWeek()
    featuredItem = db.session.query(WeekInfo).one().featuredItem
    return render_template("index.html", recipes=recipes[:5], winnerRecipes = winnerRecipes, featuredItem = featuredItem)


@mod_main.route('/login')
def login():
        return redirect(url_for('mod_auth.login'))

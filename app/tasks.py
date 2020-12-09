from flask_apscheduler import APScheduler
from datetime import date, timedelta
from calendar import weekday

from sqlalchemy import desc
from app.config import FeaturedIngredients
from random import choice
scheduler = APScheduler()


def checkNewWeek():
    app = scheduler.app
    with app.app_context():
        today = date.today()
        last_monday = today - timedelta(days=today.weekday())
        if db.session.query(WeekInfo).count() == 0:
            initFirstWeek()
            return

        lastWipe = db.session.query(WeekInfo).one().lastWipeDate
        if lastWipe < last_monday:
            saveStandings()
            wipeWeek(today)
            generateNewFeaturedItem()
            

def saveStandings():
    db.session.query(LastWeeksWinners).delete()
    recipes = Recipe.query.order_by(desc(Recipe.total_likes)).limit(3)
    for recipe in recipes:
        recipeCopy = LastWeeksWinners(id = recipe.id, title = recipe.title, ingredients = recipe.ingredients, instructions = recipe.instructions, username = recipe.username, date_created = recipe.date_created, total_likes = recipe.total_likes)
        db.session.add(recipeCopy)
        db.session.commit()
    

def wipeWeek(today):
    db.session.query(CompetingRecipes).delete()
    setattr(db.session.query(WeekInfo).one(), 'lastWipeDate', today)
    db.session.commit()

def generateNewFeaturedItem():
    setattr(db.session.query(WeekInfo).one(), 'featuredItem', getRandomFeturedItem())
    db.session.commit()

def getRandomFeturedItem():
    return choice(FeaturedIngredients.possibleItems)

def initFirstWeek():
        today = date.today()
        curDate = WeekInfo(lastWipeDate = today, featuredItem = getRandomFeturedItem())
        db.session.add(curDate)
        db.session.commit()
    
from app.dbschema.recipe import CompetingRecipes, Recipe
from app.dbschema.weeklyWipe import WeekInfo, LastWeeksWinners
from app.app import db
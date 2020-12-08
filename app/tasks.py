from flask_apscheduler import APScheduler
from datetime import date, timedelta
from calendar import weekday
from app.dbschema.recipe import CompetingRecipes, Recipe
from app.dbschema.weeklyWipe import LastWeeklyWipe, LastWeeksWinners
from app import db
from sqlalchemy import desc
scheduler = APScheduler()


def checkNewWeek():
    app = scheduler.app
    with app.app_context():
        today = date.today()
        last_monday = today - timedelta(days=today.weekday())
        if db.session.query(LastWeeklyWipe).count() == 0:
            curDate = LastWeeklyWipe(date = last_monday)
            db.session.add(curDate)
            db.session.commit()
            return

        lastWipe = db.session.query(LastWeeklyWipe).one().date
        saveStandings()
        if lastWipe < last_monday:
            saveStandings()
            wipeWeek(today)
            

def saveStandings():
    db.session.query(LastWeeksWinners).delete()
    recipes = Recipe.query.order_by(desc(Recipe.total_likes)).limit(3)
    for recipe in recipes:
        recipeCopy = LastWeeksWinners(id = recipe.id, title = recipe.title, ingredients = recipe.ingredients, instructions = recipe.instructions, username = recipe.username, date_created = recipe.date_created, total_likes = recipe.total_likes)
        db.session.add(recipeCopy)
        db.session.commit()
    

def wipeWeek(today):
    db.session.query(CompetingRecipes).delete()
    setattr(db.session.query(LastWeeklyWipe).one(), 'date', today)
    db.session.commit()

    
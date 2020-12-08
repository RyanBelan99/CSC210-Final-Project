from flask_apscheduler import APScheduler
from datetime import date, timedelta
from calendar import weekday
from app.dbschema.recipe import LastWeeklyWipe, CompetingRecipes
from app import db
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
        if lastWipe < last_monday:
            db.session.query(CompetingRecipes).delete()
            setattr(db.session.query(LastWeeklyWipe).one(), 'date', today)
            db.session.commit()

    
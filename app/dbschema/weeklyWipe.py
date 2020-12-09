from app.app import db

class WeekInfo(db.Model):
    __tablename__ = 'lastWeeklyWipe'
    lastWipeDate = db.Column(db.Date, primary_key=True)
    featuredItem = db.Column(db.String(100), nullable=False)

class LastWeeksWinners(db.Model):
    __tablename__ = 'LastWeeksWinners'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.PickleType, nullable=False)
    instructions = db.Column(db.PickleType, nullable=False)
    username = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    total_likes = db.Column(db.Integer, nullable=False)
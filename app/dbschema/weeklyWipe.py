from app import db

class LastWeeklyWipe(db.Model):
    __tablename__ = 'lastWeeklyWipe'
    date = db.Column(db.Date, primary_key=True)

class LastWeeksWinners(db.Model):
    __tablename__ = 'LastWeeksWinners'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.PickleType, nullable=False)
    instructions = db.Column(db.PickleType, nullable=False)
    username = db.Column(db.Integer, nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)
    total_likes = db.Column(db.Integer, nullable=False)
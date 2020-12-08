from app import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.PickleType, nullable=False)
    instructions = db.Column(db.PickleType, nullable=False)
    username = db.Column(db.Integer, db.ForeignKey('users.username'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    liked = db.relationship('LikePost', backref='recipe', lazy='dynamic')
    total_likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Recipe %r>' % self.title

    @hybrid_property
    def likes(self):
        return self.liked.count()

    def addLike(self):
        self.total_likes = self.total_likes + 1

    def removeLike(self):
        self.total_likes = self.total_likes - 1

class CompetingRecipes(db.Model):
    __tablename__ = 'competingRecipes'
    id = db.Column(db.Integer, primary_key=True)

class LastWeeklyWipe(db.Model):
    __tablename__ = 'lastWeeklyWipe'
    date = db.Column(db.Date, primary_key=True)

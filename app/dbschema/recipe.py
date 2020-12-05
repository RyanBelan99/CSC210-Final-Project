from app import db
from datetime import datetime
from sqlalchemy.ext.hybrid import hybrid_property
class Recipe(db.Model):
    __tablename__ = 'recipe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.PickleType, nullable=False)
    instructions = db.Column(db.PickleType, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    liked = db.relationship('LikePost', backref='recipe', lazy='dynamic')

    def __repr__(self):
        return '<Recipe %r>' % self.title

    @hybrid_property
    def likes(self):
        return self.liked.count()

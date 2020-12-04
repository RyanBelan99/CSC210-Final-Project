from app import db
from datetime import datetime
class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    ingredients = db.Column(db.String(1000), nullable=False)
    instructions = db.Column(db.String(1000), nullable=False)
    #user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Recipe: %r>' % self.title

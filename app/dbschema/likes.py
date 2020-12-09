from flask import Flask
from app.app import db

class LikePost(db.Model):
    __tablename__ = 'likepost'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __repr__(self):
        return '<Like id %r>' % self.id

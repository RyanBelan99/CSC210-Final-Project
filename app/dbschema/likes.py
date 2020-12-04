from flask import Flask
from app import db

class LikePost(db.Model):
    __tablename__ = 'likepost'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))

    def __repr__(self):
        return '<Like id %r>' % self.id

# class LikeTotals(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True, autoincrement=True)
#     name = db.Column(db.String(20))
#     birth = db.Column(db.String(10), nullable = False)
#     username = db.Column(db.String(64), unique=True, index=True)
#     password = db.Column(db.String(128))
#     recipes = db.relationship('Recipe', backref='users', lazy=True)
#
#     def __repr__(self):
#         return '<User %r>' % self.username

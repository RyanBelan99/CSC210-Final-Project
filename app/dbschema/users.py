from flask import Flask
from flask_login import UserMixin
from app.app import db
from app.dbschema.recipe import Recipe
from app.dbschema.likes import LikePost

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    name = db.Column(db.String(20))
    birth = db.Column(db.String(10), nullable = False)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='users', lazy=True)
    liked = db.relationship('LikePost', foreign_keys='LikePost.user_id', backref='users', lazy='dynamic')


    def __init__(self,name,birth,username,password):
        self.name = name
        self.birth = birth
        self.username = username
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username

    def like(self, recipe):
        if  LikePost.query.filter(LikePost.user_id == self.id, LikePost.recipe_id == recipe.id).count() > 0:
            LikePost.query.filter_by(user_id=self.id, recipe_id=recipe.id).delete()
            recipe.removeLike()
            db.session.commit()
        else:
            like = LikePost(user_id=self.id, recipe_id=recipe.id)
            db.session.add(like)
            recipe.addLike()
            db.session.commit()

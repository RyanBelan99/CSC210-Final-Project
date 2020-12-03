from flask import Flask
from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username

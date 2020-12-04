from flask import Flask
from flask_login import UserMixin
from app import db
from app.dbschema.recipe import Recipe

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    birth = db.Column(db.String(10), nullable = False)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))
    #role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))


    def __init__(self,name,birth,username,password):
        self.name = name
        self.birth = birth
        self.username = username
        self.password = password

    #recipes = db.relationship('Recipe', backref='users', lazy=True)
    def __repr__(self):
        return '<User %r>' % self.username

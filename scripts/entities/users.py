from flask import Flask
from flask_login import UserMixin

class User(UserMixin, db.list):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unquie=True, index=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

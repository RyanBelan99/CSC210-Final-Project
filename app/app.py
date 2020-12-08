from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from app import db, app

if __name__ == "__main__":
     app.run(ssl_context=('cert.pem', 'key.pem'))
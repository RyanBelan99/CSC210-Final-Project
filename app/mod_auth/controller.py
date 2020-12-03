from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.entities.models import LoginForm

mod_auth = Blueprint('mod_auth', __name__)

@mod_auth.route('/login')
def login():
    return render_template("auth/login.html")

@mod_auth.route('/login', methods=['POST'])
def login_post():
    form = LoginForm(request.form)
    if form.validate_on_submit():


    return render_template("auth/login.html", form=form)

@mod_auth.route('/signup', methods=['POST'])
def signup():
    if form.validate_on_submit():
        name = request.form.get('name')
        birth = request.form.get("birth")
        age = request.form.get("age")
        username = request.form.get('username')
        password = request.form.get('password')

    user_check = User.query.filter_by(username=username).first()

    if user_check:
        flash("This Username is Already Picked.")
        return redirect(url_for('mod_auth.signup'))     

    user_info = User(name=name, birth=birth, age=age, username=username, password=password) 
    try:
        db.session.add(user_info)
        db.session.commit()
         

    return render_template()  


@mod_auth.route('/logout')    
def logout():
    return redirect(url_for('mod_main.index.html')) 



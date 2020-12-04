from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from app import db
from app.entities.models import LoginForm, SignupForm
from app.dbschema.users import User
from werkzeug.security import generate_password_hash, check_password_hash

mod_auth = Blueprint('mod_auth', __name__)

@mod_auth.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        return render_template('user/profile.html')
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if not check_password_hash(user.password, password) and not user:
            flash("Password or Username is Incorrect")
            return redirect(url_for('mod_auth.login'))
        login_user(user)
        return render_template('user/profile.html')
    return render_template('auth/login.html', form=form)

@mod_auth.route('/signup', methods=['POST','GET'])
def signup():
    form = SignupForm(request.form)
    if form.validate_on_submit():
        return render_template('user/profile.html')
        name = request.form.get('name')
        birth = request.form.get("birth")
        username = request.form.get('username')
        password = generate_password_hash(request.form.get('password'))
        user_check = User.query.filter_by(username=username).first()
        if user_check:
            flash("This Username is Already Picked.")
            return redirect(url_for('mod_auth.signup'))
        user_info = User(name=name, birth=birth, username=username, password=password)
        db.session.add(user_info)
        db.session.commit()
        return render_template('user/profile.html')
    return render_template("auth/signup.html", form=form)


@mod_auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('mod_main.index'))

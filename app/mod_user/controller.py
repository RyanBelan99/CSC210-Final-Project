from flask import Blueprint, render_template, request, redirect, url_for
from app.entities.models import EditProfileForm, ChangePasswordForm
from flask_login import current_user
from app.dbschema.users import User
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.before_request
def checkLogn():
    if not current_user.is_authenticated:
        return redirect(url_for("mod_auth.login"))

@mod_user.route('/profile')
def profile():
    recipes = current_user.recipes
    return render_template("user/profile.html", recipes=recipes)
    

@mod_user.route('/edit', methods=['POST','GET'])
def editProfile():
    form = EditProfileForm(request.form)
    if form.validate_on_submit():
        name = request.form.get('name')
        birth = request.form.get('birth')
        user = User.query.filter_by(username=current_user.username).first()
        setattr(user, 'name', name)
        setattr(user, 'birth', birth)
        db.session.commit()
        return redirect(url_for("mod_user.profile"))
    return render_template("user/editProfile.html", form=form)

@mod_user.route('/changePassword', methods=['POST','GET'])
def changePassword():
    form = ChangePasswordForm(request.form)
    if form.validate_on_submit():
        curPassword = request.form.get('curPassword')
        newPassword = request.form.get('newPassword')
        user = User.query.filter_by(username=current_user.username).first()
        if not check_password_hash(user.password, curPassword) and not user:
            flash("Password Incorrect")
            return redirect(url_for('mod_user.changePassword'))
        password = generate_password_hash(newPassword)
        setattr(user, 'password', password)
        db.session.commit()
        return redirect(url_for("mod_user.profile"))
    return render_template("user/editProfile.html", form=form)

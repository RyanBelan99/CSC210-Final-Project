from flask import Blueprint, render_template, request, redirect, url_for
from app.entities.models import SignupForm
from flask_login import current_user

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template("user/profile.html")
    return redirect(url_for("mod_auth.login"))

@mod_user.route('/edit')
def editProfile():
        form = SignupForm(request.form)
        return render_template("user/editProfile.html", form=form)

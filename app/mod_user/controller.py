from flask import Blueprint, render_template, request
from app.entities.models import SignupForm
from flask_login import current_user

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.route('/profile')
def profile():
    if current_user.is_authenticated:
        user = current_user.name
        birthday = current_user.birth
        username = current_user.username
        return render_template("user/profile.html", user=user, birthday=birthday, username=username)
    return render_template("user/profile.html")

@mod_user.route('/edit')
def editProfile():
        form = SignupForm(request.form)
        return render_template("user/editProfile.html", form=form)

# @mod_post.route('/createPost', methods=['POST', 'GET'])
# def createPost():
#         form = PostForm(request.form)
#         return render_template("post/createPost.html", form=form)

from flask import Blueprint, render_template, request
from app.entities.models import SignupForm

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.route('/')
def profile():
        return render_template("user/profile.html")

@mod_user.route('/edit')
def editProfile():
        form = SignupForm(request.form)
        return render_template("user/editProfile.html", form=form)

# @mod_post.route('/createPost', methods=['POST', 'GET'])
# def createPost():
#         form = PostForm(request.form)
#         return render_template("post/createPost.html", form=form)
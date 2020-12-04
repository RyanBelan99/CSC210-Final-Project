from flask import Blueprint, render_template, request
from app.entities.models import PostForm

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.route('/')
def profile():
        return render_template("user/profile.html")

# @mod_post.route('/createPost', methods=['POST', 'GET'])
# def createPost():
#         form = PostForm(request.form)
#         return render_template("post/createPost.html", form=form)
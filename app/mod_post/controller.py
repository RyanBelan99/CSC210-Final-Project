from flask import Blueprint, render_template, request
from app.entities.models import PostForm

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts')
def posts():
        return render_template("post/posts.html")

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        form = PostForm(request.form)
        return render_template("post/createPost.html", form=form)
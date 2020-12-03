from flask import Blueprint, render_template, request
from app.entities.models import PostForm
from app.dbschema.recipe import Recipe

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts')
def posts():
        return render_template("post/posts.html")

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        form = PostForm(request.form)
        new_recipe = Recipe(title = form.title, ingredients = form.ingredients, instructions = form.instructions)

        try:
            db.session.add(new_recipe)
            db.session.commit()
            return redirect('post/posts.html')
        except:
            return "There was an error adding a new recipe"
        #return render_template("post/posts.html", form=form)

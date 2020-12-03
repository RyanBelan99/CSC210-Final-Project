from flask import Blueprint, render_template, request, redirect
from app import db
from app.entities.models import PostForm
from app.dbschema.recipe import Recipe

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts')
def posts():
        return render_template("post/posts.html")

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        #if request.method == 'POST':
        #    form = PostForm(request.form)
        #     new_recipe = Recipe(title = form.title, ingredients = form.ingredients, instructions = form.instructions)
        #
        #     try:
        #         db.session.add(new_recipe)
        #         db.session.commit()
        #         return redirect('post/posts.html')
        #     except:
        #         return "There was an error adding a new recipe"
        # else:
        #     recipes = Recipe.query.order_by(Recipe.date_created)
        # return render_template("post/createPost.html", form=form, recipes=recipes)

        form = PostForm(request.form)
        if form.validate_on_submit():
            new_recipe = Recipe(title = form.title, ingredients = form.ingredients, instructions = form.instructions)
            try:
                db.session.add(new_recipe)
                db.session.commit()
                return render_template("post/posts.html")
            except:
                return "There was an error adding a new recipe"
        else:
            recipes = Recipe.query.order_by(Recipe.date_created)
            return render_template("post/createPost.html", form=form)

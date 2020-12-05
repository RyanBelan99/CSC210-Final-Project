from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.entities.models import PostForm
from app.dbschema.recipe import Recipe
from flask_login import current_user

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts', methods=['POST', 'GET'])
def posts():
        recipes = Recipe.query.order_by(Recipe.date_created)
        return render_template("post/posts.html", recipes=recipes)

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        form = PostForm(request.form)
        if current_user.is_authenticated:
            if form.validate_on_submit():
                ingredientList = ' '.join(form.ingredients.data).split()
                instructionList = ' '.join(form.instructions.data).split()
                new_recipe = Recipe(title = form.title.data, ingredients = ingredientList, instructions = instructionList, user_id=current_user.id)
                try:
                    db.session.add(new_recipe)
                    db.session.commit()
                    recipes = Recipe.query.order_by(Recipe.date_created)
                    return redirect(url_for('mod_post.posts'))
                except:
                    return "There was an error adding a new recipe"
            else:
                return render_template("post/createPost.html", form=form)
        else:
            return redirect(url_for('mod_auth.login'))

@mod_post.route('/likePost/<recipe_id>', methods=['POST', 'GET'])
def likePost(recipe_id):
    form = LikeForm(request.form)
    if form.validate_on_submit():#current_user.is_authenticated:
        recipe = Recipe.query.filter_by(id=recipe_id)
        return render_template("post/posts.html", form=form)

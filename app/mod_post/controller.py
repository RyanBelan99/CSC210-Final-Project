from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.entities.models import PostForm, LikeForm
from app.dbschema.recipe import Recipe
from app.dbschema.likes import LikePost
from sqlalchemy import desc
from flask_login import current_user

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts', methods=['POST', 'GET'])
def posts():
        recipes = Recipe.query.order_by(desc(Recipe.date_created))
        form = LikeForm(request.form)
        usernames=[]
        for recipe in recipes:
            usernames.append(Recipe.query.filter_by(id=recipe.id).first_or_404().username)
        return render_template("post/posts.html", recipes=recipes, form=form, usernames=usernames)

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        form = PostForm(request.form)
        if current_user.is_authenticated:
            if form.validate_on_submit():
                ingredientList = list(filter(None, form.ingredients.data))
                instructionList = list(filter(None, form.instructions.data))
                new_recipe = Recipe(title = form.title.data, ingredients = ingredientList, instructions = instructionList, username=current_user.username, total_likes=0)
                try:
                    db.session.add(new_recipe)
                    db.session.commit()
                    recipes = Recipe.query.order_by(desc(Recipe.date_created))
                    return redirect(url_for('mod_post.posts'))
                except:
                    return "There was an error adding a new recipe"
            else:
                return render_template("post/createPost.html", form=form)
        else:
            return redirect(url_for('mod_auth.login'))

@mod_post.route('/likePost/<int:recipe_id>', methods=['POST', 'GET'])
def likePost(recipe_id):
    if current_user.is_authenticated and current_user.username != Recipe.query.filter_by(id=recipe_id).first_or_404().username:
        recipe = Recipe.query.filter_by(id=recipe_id).first_or_404()
        current_user.like(recipe)
        db.session.commit()
    return redirect(url_for("mod_post.posts"))

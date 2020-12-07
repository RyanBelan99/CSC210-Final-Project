from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.dbschema.users import User
from app.entities.models import PostForm, LikeForm, EditRecipeForm
from app.dbschema.recipe import Recipe
from app.dbschema.likes import LikePost
from sqlalchemy import desc
from flask_login import current_user

mod_post = Blueprint('mod_post', __name__)

@mod_post.route('/posts', methods=['POST', 'GET'])
def posts():
        recipes = Recipe.query.order_by(desc(Recipe.date_created))
        form = LikeForm(request.form)
        return render_template("post/posts.html", recipes=recipes, form=form)

@mod_post.route('/createPost', methods=['POST', 'GET'])
def createPost():
        form = PostForm(request.form)
        if current_user.is_authenticated:
            if form.validate_on_submit():
                ingredientList = ' '.join(form.ingredients.data).split()
                instructionList = ' '.join(form.instructions.data).split()
                new_recipe = Recipe(title = form.title.data, ingredients = ingredientList, instructions = instructionList, user_id=current_user.id, total_likes=0)
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
    if current_user.is_authenticated:
        recipe = Recipe.query.filter_by(id=recipe_id).first_or_404()
        current_user.like(recipe)
        db.session.commit()
        return redirect(url_for("mod_post.posts"))

@mod_post.route('/editPost/<int:recipe_id>', methods=['POST','GET'])
def editPost(recipe_id):
    edit_form = EditRecipeForm(request.edit_form)
    if edit_form.validate_on_submit():
        title = request.edit_form.get('title')
        ingredients = request.edit_form.get('newIngredients')
        instructions = request.edit_form.get('newInstructions')
        recipe_user = Recipe.query.filter_by(id=recipe_id)
        setattr(recipe_user, 'title', title)
        setattr(recipe_user,'ingredient', ingredients)
        setattr(recipe_user,'instructions', instructions)
        try:
            db.session.commit()
        except:
            return "Error editing from database"
    else:
        return render_template("post/posts.html", edit_form=edit_form)


@mod_post.route('/deletePost/<recipe_id>', methods=['POST','GET'])
def deletePost(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    print(recipe)
    db.session.delete(recipe)
    try:
        db.session.commit()
    except:
	    return "Error deleting from database"
    return redirect(url_for("mod_post.posts"))


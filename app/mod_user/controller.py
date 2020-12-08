from flask import Blueprint, render_template, request, redirect, url_for
from app.entities.models import EditProfileForm, ChangePasswordForm, EditRecipeForm, LikeForm
from flask_login import current_user
from app.dbschema.users import User
from app.dbschema.recipe import Recipe
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

mod_user = Blueprint('mod_user', __name__, url_prefix='/user')

@mod_user.before_request
def checkLogn():
    if not current_user.is_authenticated:
        return redirect(url_for("mod_auth.login"))

@mod_user.route('/profile')
def profile():
    recipes = current_user.recipes
    recipes.sort(key=lambda x: x.date_created, reverse=True)
    return render_template("user/profile.html", recipes=recipes)

@mod_user.route('/edit', methods=['POST','GET'])
def editProfile():
    form = EditProfileForm(request.form)
    if form.validate_on_submit():
        name = request.form.get('name')
        birth = request.form.get('birth')
        user = User.query.filter_by(username=current_user.username).first()
        setattr(user, 'name', name)
        setattr(user, 'birth', birth)
        db.session.commit()
        return redirect(url_for("mod_user.profile"))
    return render_template("user/editProfile.html", form=form)

@mod_user.route('/changePassword', methods=['POST','GET'])
def changePassword():
    form = ChangePasswordForm(request.form)
    if form.validate_on_submit():
        curPassword = request.form.get('curPassword')
        newPassword = request.form.get('newPassword')
        user = User.query.filter_by(username=current_user.username).first()
        if not check_password_hash(user.password, curPassword) and not user:
            flash("Password Incorrect")
            return redirect(url_for('mod_user.changePassword'))
        password = generate_password_hash(newPassword)
        setattr(user, 'password', password)
        db.session.commit()
        return redirect(url_for("mod_user.profile"))
    return render_template("user/editProfile.html", form=form)

@mod_user.route('/editPost/<int:recipe_id>', methods=['POST','GET'])
def editPost(recipe_id):
    form = EditRecipeForm(request.form)
    print("test")
    if form.validate_on_submit():
        print("test test")
        title = request.form.get('title')
        ingredients = request.form.get('newIngredients')
        instructions = request.form.get('newInstructions')
        recipe_user = Recipe.query.filter_by(id=recipe_id).first()
        setattr(recipe_user, 'title', title)
        setattr(recipe_user,'ingredient', ingredients)
        setattr(recipe_user,'instructions', instructions)
        try:
            db.session.commit()
            return redirect(url_for("mod_user.profile"))
        except:
            return "Error editing from database"
    else:
        return render_template("user/editPost.html", form=form)

@mod_user.route('/deletePost/<recipe_id>', methods=['POST','GET'])
def deletePost(recipe_id):
    recipe = Recipe.query.get(recipe_id)
    print(recipe)
    db.session.delete(recipe)
    try:
        db.session.commit()
    except:
	    return "Error deleting from database"
    return redirect(url_for("mod_user.profile"))





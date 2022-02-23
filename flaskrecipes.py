from flask import Flask, render_template, url_for, flash, redirect
from recipes import Recipes
app = Flask(__name__)

# #generate using secrets module
# app.config['SECRET_KEY'] = '827113b2ab268dadc058d67ecc0dca6fe2948a2db8097341'

# recipes = [
#     {
#         "author": "Sally",
#         "recipe_name": "chicken alfredo",
#         "ingredient": "chicken",
#         "calories": "120"
#     },
#     {
#         "author": "Alan",
#         "recipe_name": "noodles",
#         "ingredient": "soup",
#         "calories": "300"
#     }
# ]

recipes = Recipes()
recipes_obj = recipes.all()

@app.route("/")
@app.route("/recipes", methods=["GET"])
# @app.route("/home")
def home_page():
    return render_template('home.html', recipes=recipes_obj)


@app.route("/recipe/<recipe_name>", methods=["GET"])
def recipe_page(recipe_name):
    recipe_ingredients= recipes_obj[recipe_name][0]
    recipe_link = recipes_obj[recipe_name][2][0]
    return render_template('display_recipe.html', recipe_name = recipe_name, recipe_link = recipe_link, recipe_ingredients=recipe_ingredients)

@app.route("/recipes/<chosen_tag>", methods=["GET"])
def tag_page(chosen_tag):
    recipe_of_chosen_category = {}
    for indiv_recipe in recipes_obj:
        if chosen_tag in recipes_obj[indiv_recipe][1]:
            recipe_of_chosen_category[indiv_recipe] = recipes_obj[indiv_recipe]
    return render_template('home.html', recipes = recipe_of_chosen_category)
    # recipe_ingredients= recipes_obj[recipe_name][0]
    # recipe_link = recipes_obj[recipe_name][2][0]
    # return render_template('display_recipe.html', recipe_name = recipe_name, recipe_link = recipe_link, recipe_ingredients=recipe_ingredients)


# @app.route("/favorites")
# def about_page():
#     return "<p>About this site</p>"

# @app.route("/register", methods=["GET", "POST"])
# def register_page():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f"Account created successfully for {form.username.data}.", "success")
#         return redirect(url_for("home_page"))
#     return render_template('register.html', title='Register', form=form)

# @app.route("/login", methods=["GET", "POST"])
# def login_page():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.username.data == "sally" and form.password.data == "password":
#             flash(f"Logged in!!", "success")
#             return redirect(url_for("home_page"))
#         else:
#             flash(f"Logged failed - Try again!!", "danger")
#     return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
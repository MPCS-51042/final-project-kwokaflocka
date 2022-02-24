from flask import Flask, render_template, url_for, flash, redirect
from recipes import Recipes
from recipe import Recipe

app = Flask(__name__)

recipes = Recipes()
recipes_dict = recipes.all_dicts()
recipes_objs = recipes.all_objs()

#get the calories:
# specific_dish = recipes_objs["Fresh Pasta"]
# calories = specific_dish.get_ingredient_calories()
# print(type(calories))


@app.route("/")
@app.route("/recipes", methods=["GET"])
def home_page():
    return render_template('home.html', recipes=recipes_dict)


@app.route("/recipe/<recipe_name>", methods=["GET"])
def recipe_page(recipe_name):
    recipe_ingredients= recipes_dict[recipe_name][0]
    recipe_link = recipes_dict[recipe_name][2][0]

    # #get the calories:
    # specific_dish = recipes_objs[recipe_name]
    # calories = specific_dish.get_ingredient_calories()
    # print(calories)
    return render_template('display_recipe.html', recipe_name = recipe_name, recipe_link = recipe_link, recipe_ingredients=recipe_ingredients)

@app.route("/recipes/<chosen_tag>", methods=["GET"])
def tag_page(chosen_tag):
    recipe_of_chosen_category = {}
    for indiv_recipe in recipes_dict:
        if chosen_tag in recipes_dict[indiv_recipe][1]:
            recipe_of_chosen_category[indiv_recipe] = recipes_dict[indiv_recipe]
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
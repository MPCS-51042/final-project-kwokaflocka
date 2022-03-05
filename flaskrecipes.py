import re
from fastapi import FastAPI, Query
from pydantic import BaseModel
from fastapi import HTTPException
from recipes import Recipes
from recipe import Recipe
from typing import List, Optional

app = FastAPI()
app.db = Recipes()

class RecipeModel(BaseModel):
    recipe_name: str
    recipe_link: str
    recipe_ingredients: dict
    recipe_categories: list
    recipe_note: str

class IngredientsModel(BaseModel):
    ingredients_list: list

class NotesModel(BaseModel):
    recipe_name: str
    recipe_note: str

@app.get('/')
def all_the_recipes():
    return app.db.all()

@app.get('/recipes')
def all_the_recipes():
    return app.db.all()

#works
@app.get('/recipes/{recipe_name}')
def get_specific_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not an item in the database")
    return app.db.get_recipe(recipe_name)

#works
@app.get('/recipes-nutrition/{recipe_name}')
def get_recipe_nutrition(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not an item in the database")
    return app.db.get_recipe_nutrition(recipe_name)

#works
@app.get('/diet/{diet_name}')
def get_diet_recipe(diet_name):
    diet_name = diet_name.lower()
    if diet_name not in app.db.get_diets():
        raise HTTPException(status_code=400, detail="Not a supported diet")
    return app.db.get_best_diet_options(diet_name)

#still working
#the returned recipes are sorted in what is the best option objectively you have 
#for successfully making hte recipe for the list of ingredients you have in your pantry 
@app.get('/what_can_i_make/{recipe_name}')
def get_close_recipes_with_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not a recipe in the cook book :(")
    return app.db.get_close_recipes(recipe_name)

@app.get('/simplest/{ingredient_name}')
def get_simplest(ingredient_name):
    ingredient_name = ingredient_name.lower()
    return app.db.get_simplest(ingredient_name)

# {
#   "recipe_name": "potato",
#   "recipe_link": "www.potato.com",
#   "recipe_ingredients": {"oil": "1tbsp", "potato": "3whole"},
#   "recipe_categories": [
#     "side dish"
#   ]
# }
@app.post('/new-recipe')
def add_new_recipe(recipe: RecipeModel):
    name = recipe.recipe_name.lower()
    link = recipe.recipe_link.lower()

    if len(recipe.recipe_ingredients) == 0:
        raise HTTPException(status_code=400, detail="Not a supported diet")

    #ensure the amount of the ingredient is a combinations of (###str) so it is likely the 
    #user has specified the amount of ingredients and a unit of measure
    regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
    for key in  recipe.recipe_ingredients:
        amount_unit = recipe.recipe_ingredients[key]
        regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
        if not regex_string.match(amount_unit):
            raise HTTPException(status_code=400, detail="You must specific an ingredients amount with a unit of measurement. Ex: 1tbsp, 3whole, 1pinch")
    return app.db.put(name, link, recipe.recipe_ingredients, recipe.recipe_categories, recipe.recipe_note)

#TEST

# #TODO
# @app.post('/update')
# def update(recipe: RecipeModel):
#     #update recipe ingredient
#     pass

# #TODO
@app.post('/notes')
def add_note(note_to_add: NotesModel):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not an item in the database")
    return app.db.add_note(note_to_add.recipe_name, note_to_add.recipe_note)

@app.delete('/recipe')
def delete_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not an item in the database")
    return app.db.delete_recipe(recipe_name)

@app.delete('/note')
def delete_note(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=400, detail="Not an item in the database")
    return app.db.delete_note(recipe_name)









#json.dumps()
 
# @app.post('/books')
# def add_book(book_and_title: Book):
#     book_and_title_dict = book_and_title.dict()
#     app.db.put(book_and_title_dict["author"], book_and_title_dict["title"])
#     return app.db.all()

# @app.delete('/books/{author_name}')
# def delete_author(author_name: str):
#     if author_name not in app.db.all():
#         raise HTTPException(status_code=400, detail="Not an item in the database")
#     else: 
#         removed_value = app.db.delete(author_name)
#     return removed_value

#endpoint = url that someone visits to get specific data from our API


# from flask import Flask, render_template, request, url_for, flash, redirect
# from recipes import Recipes
# from recipe import Recipe


# app = Flask(__name__)

# recipes = Recipes()
# recipes_dict = recipes.all_dicts()
# recipes_objs = recipes.all_objs()

# #get the calories:
# # specific_dish = recipes_objs["Fresh Pasta"]
# # calories = specific_dish.get_ingredient_calories()
# # print(type(calories))


# # @name_space.route("/")
# # @name_space.route("/recipes", methods=["GET"])
# # def home_page():
# #     #return render_template('home.html', recipes=recipes_dict)


# # @name_space.route("/recipe/<recipe_name>", methods=["GET"])
# # def recipe_page(recipe_name):
# #     recipe_ingredients= recipes_dict[recipe_name][0]
# #     recipe_link = recipes_dict[recipe_name][2][0]

# #     # #get the calories:
# #     # specific_dish = recipes_objs[recipe_name]
# #     # calories = specific_dish.get_ingredient_calories()
# #     # print(calories)
# #     #return render_template('display_recipe.html', recipe_name = recipe_name, recipe_link = recipe_link, recipe_ingredients=recipe_ingredients)

# # @name_space.route("/recipes/<chosen_tag>", methods=["GET"])
# # def tag_page(chosen_tag):
# #     recipe_of_chosen_category = {}
# #     for indiv_recipe in recipes_dict:
# #         if chosen_tag in recipes_dict[indiv_recipe][1]:
# #             recipe_of_chosen_category[indiv_recipe] = recipes_dict[indiv_recipe]
# #     #return render_template('home.html', recipes = recipe_of_chosen_category)

# #########################################################################################################

# @name_space.route('/basic_api/entities', methods=['GET', 'POST'])
# def entities():
#     if request.method == "GET":
#         return {
#             'message': 'This endpoint should return a list of entities',
#             'method': request.method
#         }
#     if request.method == "POST":
#         return {
#             'message': 'This endpoint should create an entity',
#             'method': request.method,
# 		'body': request.json
#         }

# @name_space.route('/basic_api/entities/<int:entity_id>', methods=['GET', 'PUT', 'DELETE'])
# def entity(entity_id):
#     if request.method == "GET":
#         return {
#             'id': entity_id,
#             'message': 'This endpoint should return the entity {} details'.format(entity_id),
#             'method': request.method
#         }
#     if request.method == "PUT":
#         return {
#             'id': entity_id,
#             'message': 'This endpoint should update the entity {}'.format(entity_id),
#             'method': request.method,
# 		'body': request.json
#         }
#     if request.method == "DELETE":
#         return {
#             'id': entity_id,
#             'message': 'This endpoint should delete the entity {}'.format(entity_id),
#             'method': request.method
#         }

# # @app.route("/favorites")
# # def about_page():
# #     return "<p>About this site</p>"

# # @app.route("/register", methods=["GET", "POST"])
# # def register_page():
# #     form = RegistrationForm()
# #     if form.validate_on_submit():
# #         flash(f"Account created successfully for {form.username.data}.", "success")
# #         return redirect(url_for("home_page"))
# #     return render_template('register.html', title='Register', form=form)

# # @app.route("/login", methods=["GET", "POST"])
# # def login_page():
# #     form = LoginForm()
# #     if form.validate_on_submit():
# #         if form.username.data == "sally" and form.password.data == "password":
# #             flash(f"Logged in!!", "success")
# #             return redirect(url_for("home_page"))
# #         else:
# #             flash(f"Logged failed - Try again!!", "danger")
# #     return render_template('login.html', title='Login', form=form)


# if __name__ == '__main__':
#     app.run(debug=True)
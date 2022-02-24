from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()
#pp.db = DataBase()

class Book(BaseModel):
    author: str
    title: str

@app.get('/')
def all_the_books():
    return "hello"

# @app.get('/books')
# def all_the_books():
#     return app.db.all()

# @app.get('/books/{author_name}')
# def get_books_of_author(author_name):
#     author_name = author_name.lower()
#     if author_name not in app.db.all():
#         raise HTTPException(status_code=400, detail="Not an item in the database")
#     return app.db.get(author_name)

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
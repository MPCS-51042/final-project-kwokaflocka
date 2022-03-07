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
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.get_recipe(recipe_name)

#works
@app.get('/recipes-nutrition/{recipe_name}')
def get_recipe_nutrition(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.get_recipe_nutrition(recipe_name)

#works
@app.get('/diet/{diet_name}')
def get_diet_recipe(diet_name):
    diet_name = diet_name.lower()
    if diet_name not in app.db.get_diets():
        raise HTTPException(status_code=404, detail="Not a supported diet")
    return app.db.get_best_diet_options(diet_name)

#still working
#the returned recipes are sorted in what is the best option objectively you have 
#for successfully making hte recipe for the list of ingredients you have in your pantry 
@app.get('/what-can-i-make/{recipe_name}')
def get_close_recipes_with_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.get_close_recipes(recipe_name)

@app.get('/simplest/{ingredient_name}')
def running_low_on(ingredient_name):
    ingredient_name = ingredient_name.lower()
    return app.db.get_smallest_amount_recipe(ingredient_name)

# {
#   "recipe_name": "potato",
#   "recipe_link": "www.potato.com",
#   "recipe_ingredients": {"oil": "1tbsp", "potato": "3whole"},
#   "recipe_categories": [
#     "side dish"
#   ],
#   "recipe_note": "Feel free to use however much oil you want"
# }
@app.post('/new-recipe')
def add_new_recipe(recipe: RecipeModel):
    name = recipe.recipe_name.lower()
    link = recipe.recipe_link.lower()

    if len(recipe.recipe_ingredients) == 0:
        raise HTTPException(status_code=400, detail="You need to provide ingredients for your recipe.")

    #ensure the amount of the ingredient is a combinations of (###str) so it is likely the 
    #user has specified the amount of ingredients and a unit of measure
    regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
    for key in  recipe.recipe_ingredients:
        amount_unit = recipe.recipe_ingredients[key]
        regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
        if not regex_string.match(amount_unit):
            raise HTTPException(status_code=400, detail="You must specify an ingredients amount with a unit of measurement. Ex: 1tbsp, 3whole, 1pinch")

    return app.db.put(name, link, recipe.recipe_ingredients, recipe.recipe_categories, recipe.recipe_note)

#TEST

@app.post('/update')
def update(recipe_name: str, recipe_ingredients: dict):
    #update recipe ingredient
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    
    regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
    for key in  recipe_ingredients:
        amount_unit = recipe_ingredients[key]
        regex_string = re.compile(r"^\d*[.,]?\d*[a-zA-Z ]+$")
        if not regex_string.match(amount_unit):
            raise HTTPException(status_code=400, detail="You must specify an ingredients amount with a unit of measurement. Ex: 1tbsp, 3whole, 1pinch")

    return app.db.update_recipe(recipe_name, recipe_ingredients)

@app.post('/notes')
def add_note(recipe_name: str, note: str):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.add_note(recipe_name, note)

@app.delete('/recipe')
def delete_recipe(recipe_name):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.delete_recipe(recipe_name)

@app.delete('/note')
def delete_note(recipe_name: str, note_number: int):
    recipe_name = recipe_name.lower()
    if recipe_name not in app.db.all():
        raise HTTPException(status_code=404, detail="Not a recipe in the database")
    return app.db.delete_note(recipe_name, note_number)
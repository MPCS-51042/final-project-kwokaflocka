from pandas import *
from recipe import Recipe
import re

class Recipes():
    _recipe_names = []
    _recipe_objs = {}
    _diet_types = ["keto", "low cal", "low fat", "low sugar", "low cholesterol", "high fiber", "high protein"]

    def __init__(self):
        self.populate_recipe_book()

    def populate_recipe_book(self):
        """
        Reads an Excel document with some base recipes into Recipe objects in our RecipeBook
        """
        xls = ExcelFile('recipe_ingredients.xls')
        sheet_names = xls.sheet_names

        list_of_sheets = []
        for sheet_name in sheet_names:
            list_of_sheets.append((sheet_name, read_excel(xls, sheet_name)))

        for sheet in list_of_sheets:
            #sheet[0] = name of the sheet
            #sheet[1] = the actual excel sheet
            ingredients = sheet[1]["Ingredients"].dropna().tolist()
            amount = sheet[1]["Amount"].dropna().tolist()
            unit = sheet[1]["Unit"].dropna().tolist()
            categories = sheet[1]["Category"].dropna().tolist()
            link = sheet[1]["Link"].dropna().tolist()

            temp_to_lower = (map(lambda x: x.lower(), ingredients))
            ingredients = list(temp_to_lower)

            ingredient_info_dict = {}
            for i in range(len(ingredients)):
                #putting the amount and unit of the ingredient as a tuple, with the ingredient as its key
                ingredient_info_dict[ingredients[i]] = (amount[i], unit[i])

            recipe_obj = Recipe(sheet[0].lower(), link[0], ingredient_info_dict, categories)
            self._recipe_objs[sheet[0].lower()] = recipe_obj

            #adding all the recipe names (sheet names) to a list
            self._recipe_names.append(sheet[0].lower())

    def all(self):
        return self._recipe_objs
    
    def get_recipe(self, recipe_name):
        return self._recipe_objs[recipe_name]

    def get_recipe_names(self):
        return self._recipe_names

    def get_diets(self):
        return self._diet_types

    def get_recipe_nutrition(self, recipe_name):
        return self._recipe_objs[recipe_name].nutrition
    
    def get_best_diet_options(self, diet_name):
        #holds tuples of (recipe name, nutrition_label)
        recipe_to_nutrition_list = []
        for recipe in self._recipe_objs:
            recipe_to_nutrition_list.append(self._recipe_objs[recipe].get_nutrition_value(diet_name))
        
        if "low" in diet_name or diet_name == "keto":
            recipe_to_nutrition_list.sort(key=lambda x: x[1])
        else:
            recipe_to_nutrition_list.sort(key=lambda x: x[1], reverse=True)

        return recipe_to_nutrition_list

    def put(self, name, link, ingredients_dict, categories, notes):
        #the user will probs give the amount_unit as a str, we want to store it as a tuple
        for key in ingredients_dict:
            amount_unit = ingredients_dict[key]
            #res = None
            temp = re.search(r'[a-z]', amount_unit, re.I)
            if temp is not None:
                res = temp.start()
                ingredients_dict[key] = (amount_unit[:res], amount_unit[res:])

        new_recipe = Recipe(name, link, ingredients_dict, categories, notes)
        self._recipe_objs[name] = new_recipe
        return new_recipe

    def get_close_recipes(self, recipe):
        """
        Given a recipe, return the recipes that have some overlapping ingredients, sorted in percentage order of 
        recipes that have the highest composition of the overlapping ingredients

        Ex: Chrysanthemum tea ingredients: Water, tea leaves, sugar, ginger, milk
        Regular Tea: Water, tea leaves || Overlap = Water, tea leaves || Overlap percentage = 100% (2/2)
        Ginger tea: Water, ginger, jujubes, sugar || Overlap = Water, ginger, sugar || Overlap percentage = 75% (3/4)

        If there is no overlap, we ignore the recipe
        """
        base_ingredient_to_compare = self._recipe_objs[recipe].recipe_ingredients.keys()
        base = set(base_ingredient_to_compare)
        recipe_overlap = []

        for key in self._recipe_objs:
            if key != recipe:
                recipe_ingredients_dict =  self._recipe_objs[key]
                comparison_recipe_ingredients = recipe_ingredients_dict.recipe_ingredients.keys()
                comparison = set(comparison_recipe_ingredients)

                overlap = base & comparison
                overlap_percentage = round(float(len(overlap)) / len(comparison) * 100, 2)

                if overlap_percentage != 0:
                    recipe_overlap.append((key, overlap_percentage, overlap))

        recipe_overlap.sort(key=lambda x: x[1], reverse=True)
        
        recipe_overlap_info = f"If you have ingredients for {recipe}, you have:"
        for recipe in recipe_overlap:
            recipe_overlap_info += f"\n{recipe[1]}% of ingredients for {recipe[0]} - {recipe[2]}"
        return recipe_overlap_info

    def get_smallest_amount_recipe(self, ingredient):
        """
        All recipes sorted in ascending order of the recipe having the least amount of the specified ingredient
        Return the recipe with the least amount of said ingredient
        """
        has_ingredient = []
        for key in self._recipe_objs:
            recipe_ingredients_dict =  self._recipe_objs[key]

            if ingredient in recipe_ingredients_dict.recipe_ingredients:
                ingredient_amount = recipe_ingredients_dict.nutrition[ingredient][0]
                #it is very difficult to standardize the units, so use the calories as a proxy for how much 
                #ingredient, irrespective of unit of measure
                ingredient_calories = recipe_ingredients_dict.nutrition[ingredient][1]["calories"]
                has_ingredient.append((key, ingredient_amount, ingredient_calories))
        
        recipe_with_the_least = "No recipe has this ingredient."
        if len(has_ingredient) > 1:
            has_ingredient.sort(key=lambda x: x[2])
            recipe_with_the_least = has_ingredient[0][0]

        return recipe_with_the_least

    def update_recipe(self, recipe_name, ingredients):
        return self._recipe_objs[recipe_name].update_ingredients(ingredients)

    def add_note(self, recipe_name, recipe_note):
        return self._recipe_objs[recipe_name].add_note(recipe_note)

    def delete_note(self, recipe_name, note_number):
        return self._recipe_objs[recipe_name].delete_note(note_number)     

    def delete_recipe(self, key):
        return self._recipe_objs.pop(key)

    
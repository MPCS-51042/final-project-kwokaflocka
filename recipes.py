from pandas import *
from recipe import Recipe
import http.client

class Recipes():
    _recipes = {}
    _recipe_names = []
    _recipe_objs = {}

    def __init__(self):
        self.populateRecipeBook()

    def populateRecipeBook(self):
        sheet_to_df_map = {}
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

            ingredient_info_dict = {}
            for i in range(len(ingredients)):
                #putting the amount and unit of the ingredient as a tuple, with the ingredient as its key
                ingredient_info_dict[ingredients[i]] = (amount[i], unit[i])

            recipe_obj = Recipe(sheet[0], link[0], ingredient_info_dict, categories)
            self._recipe_objs[sheet[0]] = recipe_obj

            #adding all the recipe names (sheet names) to a list
            self._recipe_names.append(sheet[0])

            #main dictionary of dictionaries: 
            # name of dish = key
            # list containing the {ingredient: (amount, unit)}, list of food categories, and the recipe link
            sheet_to_df_map[sheet[0]] = [ingredient_info_dict, categories, link]
        self._recipes = sheet_to_df_map


################################

    def get(self, key):
        return self._recipes[key]

    def put(self, key, value):
        self._recipes[key] = value
    
    def all_dicts(self):
        return self._recipes

    def all_objs(self):
        return self._recipe_objs

    def get_recipe_names(self):
        return self._recipe_names

    def delete(self, key):
        self._recipes.pop(key)
        return self._recipes
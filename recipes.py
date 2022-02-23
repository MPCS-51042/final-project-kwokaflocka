from pandas import *

class Recipes():
    _recipes = {}

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
            ingredients = sheet[1]["Ingredients"].tolist()
            amount = sheet[1]["Amount"].tolist()
            unit = sheet[1]["Unit"].tolist()

            ingredient_info_dict = {}
            for i in range(len(ingredients)):
                ingredient_info_dict[ingredients[i]] = (amount[i], unit[i])

            sheet_to_df_map[sheet[0]] = ingredient_info_dict
        self._recipes = sheet_to_df_map

    def get(self, key):
        return self._recipes[key]

    def put(self, key, value):
        self._recipes[key] = value

    def all(self):
        return self._recipes

    def delete(self, key):
        self._recipes.pop(key)
        return self._recipes
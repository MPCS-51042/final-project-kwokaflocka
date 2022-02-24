import http.client
import ast

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541",
    'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
    }

class Recipe():
    #str: recipe name
    #str: link
    #dictionary: {favorite:
    #             {dessert:
    #              {breakfast}}}
    #dictionary: ingredient: amount_unit

    def __init__(self, name, link, ingredients_dict, categories = []):
        self.recipe_name = name
        self.recipe_link = link
        self.recipe_ingredients = ingredients_dict
        self.category_dict = categories
        pass

    def get_ingredient_calories(self):
        calorie_list = []

        calorie_api_query_string = "/v1/nutrition?query="
        for ingredient in self.recipe_ingredients:
            amount_unit = self.recipe_ingredients[ingredient]
            calorie_api_query_string += f"{amount_unit[0]}{amount_unit[1]}{ingredient},"


        conn.request("GET", calorie_api_query_string, headers=headers)
        res = conn.getresponse()

        #byte of dictionary
        data = res.read()

        #convert into Python dictionary
        data_as_dict_str = data.decode("UTF-8")
        data_dict = ast.literal_eval(data_as_dict_str)
        return data_dict

    # def get_dish_calories(self):
    #     pass
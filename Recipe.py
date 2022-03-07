import http.client
import ast
import re

conn = http.client.HTTPSConnection("calorieninjas.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "ce19d0164fmsh3d383efc0e85ce5p16dcb1jsnb1a4a3c79541",
    'x-rapidapi-host': "calorieninjas.p.rapidapi.com"
    }

class Recipe():

    def __init__(self, name, link, ingredients_dict, categories = [], notes = []):
        self.recipe_name = name
        self.recipe_link = link
        self.recipe_ingredients = ingredients_dict
        self.category_dict = categories
        self.nutrition = self.get_nutrition()
        self.notes = notes

    def get_nutrition(self):
        nutrition_per_ingredient = {}

        for ingredient in self.recipe_ingredients:
            nutrition_per_ingredient[ingredient] = self.calculate_nutrition_one_ingredient(ingredient)

        return nutrition_per_ingredient

    def get_nutrition_value(self, diet):
        #["keto", "low cal", "low fat", "low sugar", "low cholesterol", "high fiber", "high protein"]
        if diet == "keto":
            pass
        
        diet_index = {"low cal": "calories", 
                    "low fat": "fat_saturated_g",
                    "low cholesterol": "cholesterol_mg",
                    "high fiber": "fiber_g",
                    "high protein": "protein_g"}

        nutrition_value_recipe = 0

        for ingredient in self.nutrition:
            if diet == "keto":
                carbs = self.nutrition[ingredient][1]["carbohydrates_total_g"]
                dietary_fiber = self.nutrition[ingredient][1]["fiber_g"]
                nutrition_value_ingredient = carbs-dietary_fiber
            else:
                nutrition_value_ingredient = self.nutrition[ingredient][1][diet_index[diet]]
            nutrition_value_recipe += nutrition_value_ingredient
        
        return (self.recipe_name, round(nutrition_value_recipe,2))

    # getting one ingredient at a time because the api will only return 2 at once anyways...maybe because its the 
    # free version?       
    def calculate_nutrition_one_ingredient(self, ingredient, calorie_api_query_string = "/v1/nutrition?query="):
        amount_unit = self.recipe_ingredients[ingredient]
        calorie_api_query_string += f"1 {amount_unit[1]} {ingredient},"
        calorie_api_query_string = calorie_api_query_string.replace(" ", "%20")
            
        #print(calorie_api_query_string)
        conn.request("GET", calorie_api_query_string, headers=headers)
        res = conn.getresponse()
        #byte of dictionary
        data = res.read()

        #convert into Python dictionary
        data_as_dict_str = data.decode("UTF-8")
        data_dict = ast.literal_eval(data_as_dict_str)

        #trying to put formatted amount unit into the dictionary with proper singular vs. plural forms
        amount = amount_unit[0]
        units = amount_unit[1]
        amount_unit_string = f"{amount} "
        if float(amount) > 1:
            if units != "whole":
                amount_unit_string += f"{units}s"
            else:
                if ingredient[-1] != "s":
                    amount_unit_string += f"{ingredient.lower()}s"
                else:
                    amount_unit_string += f"{ingredient.lower()}"
        else:
            amount_unit_string += f"{units}"

        #the API returns this to us in a dictionary where the key is "items" ¯\_(ツ)_/¯, and the nutrition facts is a [{}]
        #print(data_dict)
        data_dict = data_dict["items"]
        multiplier = float(amount_unit[0])
        multiplied_nutrition_dict = self.multiply_nutrition(data_dict[0], multiplier)

        #ssalllllyy
        finalized_nutrition_info = [f"{amount_unit_string}", multiplied_nutrition_dict]

        return finalized_nutrition_info

    def multiply_nutrition(self, nutrition_dict_unit_one, unit_multiplier):
        nutrition_dict_multiplied = {}
        for nutrition in nutrition_dict_unit_one:
            value = nutrition_dict_unit_one[nutrition]
            if isinstance(value, float):
                float_value_multiplied = value * unit_multiplier
                nutrition_dict_multiplied[nutrition] = round(float_value_multiplied,2)
        return nutrition_dict_multiplied

    def delete_note(self, note_number):
        if note_number < 1 or note_number > len(self.notes):
            return "That's not a valid note to delete"
        else:
            note_deleted = self.notes.pop(note_number-1)
        return note_deleted

    def add_note(self, note):
        self.notes.append(note)
        return self.notes

    def update_ingredients(self, ingredients):
        changed = []
        in_original_dict = False
        original_amount = 0
        for ingredient in ingredients:
            if ingredient in self.recipe_ingredients:
                in_original_dict = True
                original_amount = self.recipe_ingredients[ingredient]
            else:
                in_original_dict = False
            amount_unit = ingredients[ingredient]
            temp = re.search(r'[a-z]', amount_unit, re.I)
            if temp is not None:
                res = temp.start()
                new_amount = round(float(amount_unit[:res]),2)
                if new_amount == float(0):
                    self.recipe_ingredients.pop(ingredient)
                else: 
                    self.recipe_ingredients[ingredient] = (round(float(amount_unit[:res]),2), amount_unit[res:])

            if in_original_dict:
                changed_notice = f"{ingredient} amount was changed from {original_amount[0]} {original_amount[1]} to {self.recipe_ingredients[ingredient][0]} {self.recipe_ingredients[ingredient][1]}."
                changed.append(changed_notice)
            else:
                changed_notice = f"{ingredient} was added to the recipe."
                changed.append(changed_notice)

        self.nutrition = self.get_nutrition()

        return changed
     
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
        self.nutrition = self.get_nutrition()
        pass

    def get_nutrition(self):
        nutrition_per_ingredient = {}

        calorie_api_query_string = "/v1/nutrition?query="
        for ingredient in self.recipe_ingredients:
            amount_unit = self.recipe_ingredients[ingredient]
            calorie_api_query_string += f"{amount_unit[0]} {amount_unit[1]} {ingredient},"
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

            #the API returns this to us in a dictionary where the key is "items" ¯\_(ツ)_/¯
            data_dict = data_dict["items"]
            data_dict.insert(0, f"{amount_unit_string}")

            #print(type(data_dict))
            nutrition_per_ingredient[ingredient] = data_dict

            calorie_api_query_string = "/v1/nutrition?query="
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
        
        return (self.recipe_name, nutrition_value_recipe)
            
    def calculate_nutrition__one_recipe():
        amount_unit = self.recipe_ingredients[ingredient]
            calorie_api_query_string += f"{amount_unit[0]} {amount_unit[1]} {ingredient},"
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

            #the API returns this to us in a dictionary where the key is "items" ¯\_(ツ)_/¯
            data_dict = data_dict["items"]
            data_dict.insert(0, f"{amount_unit_string}")

            #print(type(data_dict))
            nutrition_per_ingredient[ingredient] = data_dict

            calorie_api_query_string = "/v1/nutrition?query="    
        pass
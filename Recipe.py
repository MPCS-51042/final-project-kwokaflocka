class Recipe():
    #str: recipe name
    #str: link
    #dictionary: {favorite:
    #             {dessert:
    #              {breakfast}}}
    #dictionary: ingredient: amount_unit

    def __init__(self, name, link, ingredients_dict, category_dict):
        self.recipe_name = name
        self.recipe_link = link
        self.recipe_ingredients = ingredients_dict
        self.category_dict = category_dict
        pass


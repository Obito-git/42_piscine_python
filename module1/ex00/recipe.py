class Recipe:
    def __new__(cls, name: str, cooking_lvl: int,
                cooking_time: int, ingredients: list,
                description: str, recipe_type: str):
        accepted_type = ["starter", "lunch", "dessert"]
        if not isinstance(name, str) or not name:
            print("Name must be not empty string")
        elif not isinstance(cooking_lvl, int) or cooking_lvl not in range(1, 6):
            print("Cooking level must be int in range 1-5")
        elif not isinstance(cooking_time, int) or cooking_time <= 0:
            print("Cooking time must be a positive integer")
        elif not isinstance(ingredients, list) or not ingredients or \
                not all(isinstance(item, str) for item in ingredients) or \
                "" in ingredients:
            print("Ingredients must be a not empty list of strings")
        elif not isinstance(description, str):
            print("Description must be a string")
        elif not isinstance(recipe_type, str) or recipe_type not in accepted_type:
            print("Recipe type must be one of \"starter\", \"lunch\" or \"dessert\"")
        else:
            return object.__new__(cls)
        return None

    def __init__(self, name: str, cooking_lvl: int,
                 cooking_time: int, ingredients: list,
                 description: str, recipe_type: str):
        """
        :param name (str): name of the recipe,
        :param cooking_lvl (int): range from 1 to 5,
        :param cooking_time (int): in minutes (no negative numbers),
        :param ingredients (list): list of all ingredients each represented by a string,
        :param description (str): description of the recipe,
        :param recipe_type (str): can be "starter", "lunch" or "dessert"
        """
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        return f"Recipe name: {self.name}\n" \
               f"Cooking lvl: {self.cooking_lvl}\n" \
               f"Cooking time: {self.cooking_time}\n" \
               f"Ingredients: {self.ingredients}\n" \
               f"Description: {self.description}\n" \
               f"Recipe type: {self.recipe_type}\n"

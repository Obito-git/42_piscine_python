from datetime import datetime
from recipe import Recipe


class Book:
    """
    name (str): name of the book,
    last_update (datetime): the date of the last update,
    creation_date (datetime): the creation date,
    recipes_list (dict): a dictionnary with 3 keys: "starter", "lunch", "dessert".
    """

    def __new__(cls, name):
        if not isinstance(name, str) or not name:
            print("Name of book must be not empty string")
            return None
        return object.__new__(cls)

    def __init__(self, name):
        self.name = name
        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            "starter": [],
            "lunch": [],
            "dessert": []
        }

    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        if not isinstance(name, str):
            print("Provided name is not a string")
            return None
        rec = None
        all_recipes = self.recipes_list["starter"] + self.recipes_list["lunch"] + self.recipes_list["dessert"]
        for item in all_recipes:
            if item.name == name:
                rec = item
                break
        if not rec:
            print(f"Can't find \"{name}\" in {self.name} cookbook")
        else:
            print(rec)
        return rec

    # ... Your code here ...
    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if not isinstance(recipe_type, str) or recipe_type not in ("started", "lunch", "dessert"):
            print("Recipe type must be one of \"started\", \"lunch\" or \"dessert\"")
            return None
        print(f"{recipe_type}:")
        if len(self.recipes_list[recipe_type]) == 0:
            print(f"They are no recipes in {recipe_type}")
        else:
            for item in self.recipes_list[recipe_type]:
                print(item)
            print()
        return [x for x in self.recipes_list[recipe_type]]

        # ... Your code here ...
    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        test = self
        if not isinstance(recipe, Recipe):
            print("Recipe must have recipe type")
            return
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)

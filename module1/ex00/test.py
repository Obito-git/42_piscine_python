from time import sleep

from book import Book
from recipe import Recipe
import sys


def recipe_test():
    print("Expecting 2 errors")
    Recipe(0, 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")

    print("\nExpecting 3 errors")
    Recipe("Recipe name", 0, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 6, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", "1", 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")

    print("\nExpecting 2 errors")
    Recipe("Recipe name", 1, "10", ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 1, -10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")

    print("\nExpecting 5 errors")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", 3], "descr", "dessert")
    Recipe("Recipe name", 1, 10, ["ing 1", "", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 1, 10, "ingr", "descr", "dessert")
    Recipe("Recipe name", 1, 10, 100, "descr", "dessert")
    Recipe("Recipe name", 1, 10, [], "descr", "dessert")

    print("\nExpecting 1 error")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], 10, "dessert")

    print("\nExpecting 4 errors")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", 123)
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "test")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "other")

    print("\n\n\nNo errors expected:")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 2, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 3, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 4, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 5, 10, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 1, 10000, ["ing 1", "ing 2", "ing 3"], "descr", "dessert")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "", "dessert")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "", "lunch")
    Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "", "starter")
    print("\n--------------------------\n")
    print(Recipe("Recipe name", 5, 10, ["ing 1", "ing 2", "ing 3"], "gggg", "dessert"))
    print(Recipe("Recipe name", 1, 10000, ["ing 1", "ing 2", "ing 3"], "descr", "lunch"))
    print(Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "", "starter"))


def book_test():
    print("Expecting 2 errors")
    Book("")
    Book(123)

    book = Book("Test")

    print("\nExpecting 3 errors")
    book.add_recipe(None)
    book.add_recipe(Recipe(1, 1, 1, 1, 1, 1))

    print("\nExpecting 4 errors")
    book.get_recipes_by_types("")
    book.get_recipes_by_types(123)
    book.get_recipes_by_types(None)
    book.get_recipes_by_types("HELLO")

    print("\nExpecting 4 errors")
    book.get_recipe_by_name("")
    book.get_recipe_by_name(None)
    book.get_recipe_by_name(123)
    book.get_recipe_by_name("Soup")

    print(f"\n\nLast update: {book.last_update}")
    print(f"Creation: {book.creation_date}")
    print("\n Waiting...\n")
    sleep(3)
    book.add_recipe(Recipe("Recipe name", 5, 10, ["ing 1", "ing 2", "ing 3"], "gggg", "dessert"))
    book.add_recipe(Recipe("Recipe name", 1, 10000, ["ing 1", "ing 2", "ing 3"], "descr", "lunch"))
    book.add_recipe(Recipe("Recipe name", 1, 10, ["ing 1", "ing 2", "ing 3"], "", "starter"))
    print(f"Last update: {book.last_update} (must be differ)")
    print(f"Creation: {book.creation_date} (must be same)")


if __name__ == "__main__":
    recipe_test()
    book_test()

cookbook = {
	"sandwich": {
		"ingredients": ["ham", "bread", "cheese", "tomatoes"],
		"meal": "lunch",
		"prep_time": 10
	},
	"cake": {
		"ingredients": ["flour", "sugar", "eggs"],
		"meal": "dessert",
		"prep_time": 60
	},
	"salad": {
		"salad": ["avocado", "arugula", "tomatoes", "spinach"],
		"meal": "lunch",
		"prep_time": 15
	}
}


def print_details(name):
	requested_recipe = cookbook.get(name)
	if requested_recipe is None:
		print(f"Can't find {name}\n")
		return
	print(f"\nRecipe for {name}:")
	print(f"Ingredients list: {requested_recipe['ingredients']}")
	print(f"To be eaten for {requested_recipe['meal']}.")
	print(f"Takes {requested_recipe['prep_time']} minutes of cooking.\n")


def print_all_names():
	print("All available recipes:")
	for elem in cookbook:
		print(elem)
	print()


def delete_recipe(name):
	requested_recipe = cookbook.get(name)
	if requested_recipe is None:
		print(f"Can't find {name}\n")
		return
	cookbook.pop(name)
	print()


def get_recipe_name():
	while True:
		try:
			print("Enter a name:")
			name = input()
			if name:
				return name
		except EOFError:
			pass


def get_recipe_meal():
	while True:
		try:
			print("Enter a meal type:")
			meal_type = input()
			if meal_type:
				return meal_type
		except EOFError:
			pass


def get_ingredients():
	ingredients = list()
	print("Enter ingredients:")
	while True:
		try:
			user_input = input()
			if user_input:
				ingredients.append(user_input)
			elif not user_input and len(ingredients) == 0:
				print("You must provide min 1 ingredient")
			else:
				return ingredients
		except EOFError:
			print("Enter ingredients:")


def get_cooking_time():
	while True:
		try:
			print("Enter a preparation time:")
			time = int(input())
			if time >= 0:
				return time
			else:
				print("Cooking time can't be negative")
		except EOFError:
			pass
		except ValueError:
			print("You need provide a number")


def add_recipe():
	name = get_recipe_name()
	cookbook[name] = {
		"ingredients": get_ingredients(),
		"meal": get_recipe_meal(),
		"prep_time": get_cooking_time()
	}


COM = "List of available option:\n\t1: Add a recipe\n\t2: Delete a recipe \
			\n\t3: Print a recipe\n\t4: Print the cookbook\n\t5: Quit\n"
if __name__ == '__main__':
	print(f"Welcome to the Python Cookbook !\n{COM}")
	while True:
		print("Please select an option:")
		try:
			res = int(input())
			print()
			if res == 1:
				add_recipe()
			elif res == 2:
				delete_recipe(get_recipe_name())
			elif res == 3:
				print_details(get_recipe_name())
			elif res == 4:
				print_all_names()
			elif res == 5:
				print("Cookbook closed.Goodbye !")
				break
			else:
				print(f"Sorry, this option does not exist.\n{COM}")
		except ValueError:
			print(f"Sorry, this option does not exist.\n{COM}")
		except EOFError:
			break


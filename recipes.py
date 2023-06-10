with open('recipes.txt', 'r', encoding='utf-8') as file:
    cook_book = {}
    for recipe_name in file:
        number_of_ingredients = int(file.readline())
        recipe_of_ingredients = []
        for i in range(number_of_ingredients):
            name_ing, count_ing, unit = file.readline().strip().split(' | ')
            recipe_of_ingredients.append({'ingredient_name': name_ing, 'quantity': count_ing, 'measure': unit})
        file.readline()
        cook_book[recipe_name.strip()] = recipe_of_ingredients
import json

cook_book = json.dumps(cook_book, indent=2, ensure_ascii=False)

print(cook_book)

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


def get_shop_list_by_dishes(dishes, person_count):
    ingredients_dish = {}
    for dish in dishes:
        for key, items in cook_book.items():
            if dish == key:
                for item in items:
                    ingredient_name, quantity, measure = item.values()
                    ingredients_dish |= {ingredient_name: {'quantity': int(quantity) * person_count, 'measure': measure}}
    return ingredients_dish


ingredients = get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)
ingredients = json.dumps(ingredients, indent=1, ensure_ascii=False)

print(ingredients)

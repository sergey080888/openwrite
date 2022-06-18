from pprint import pprint
import os
file_name = 'recipes.txt'
full_path = os.path.join(os.getcwd(), 'for_2.txt')
print(full_path)
def file_opener(file_name):
    with open(file_name) as text:
        cook_book = {}
        for line in text:
            food_name = line.strip()
            ingredients = []
            quantity_food = text.readline()
            for item in range(int(quantity_food)):
                ingredient = text.readline()
                ingredient_list = ingredient.split('|')
                ingredient_dict = {'ingredient_name': 0, 'quantity': 0, 'measure': 0 }
                n = 0
                for key in ingredient_dict:
                    if n == 1:
                        ingredient_dict[key] = int(ingredient_list[n])
                    else:
                        ingredient_dict[key] = ingredient_list[n].strip()
                    n += 1
                ingredients.append(ingredient_dict)
            cook_book[food_name] = ingredients
            text.readline()
    with open(full_path, 'w') as file_object:
        file_object.write(cook_book)

        return cook_book

pprint(file_opener(file_name), sort_dicts=False)
#
# file_opener(file_name)
# print(cook_book)

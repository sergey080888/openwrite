from pprint import pprint
# import os
file_name = 'recipes.txt'
# full_path = os.path.join(os.getcwd(), 'for_2.txt')


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
                ingredient_dict = {'ingredient_name': 0, 'quantity': 0, 'measure': 0}
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
    # with open(full_path, 'w') as file_object:
    #     file_object.write(str(cook_book))

    return cook_book


pprint(file_opener(file_name), sort_dicts=False)


def get_shop_list_by_dishes(dishes, person_count):
    cook_dict = {}
    for dish in dishes:
        if dish in file_opener(file_name).keys():
            for ingredients in file_opener(file_name)[dish]:
                if ingredients['ingredient_name'] in cook_dict.keys():
                    cook_dict[ingredients['ingredient_name']]['quantity'] += ingredients['quantity'] * person_count

                else:
                    ingredients['quantity'] = ingredients['quantity'] * person_count
                    cook_dict[ingredients['ingredient_name']] = ({'quantity': ingredients['quantity'],
                                                                  'measure': ingredients['measure']})
        else:
            print(f'{dish} блюда нет в списке')
    return cook_dict


pprint(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Буритос'], 2))
print()
pprint(get_shop_list_by_dishes(['Фахитос', 'Фахитос'], 1))
print()
pprint(get_shop_list_by_dishes(['Фахитос'], 2))



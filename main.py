file_name = 'recipes.txt'
def file_opener(file_name):
    with open(file_name) as text:
        cook_book = {}
        for line in text:
            food_name = line

            quantity = text.readline()
            cook_book[food_name] = []
            for item in range(int(quantity)):
                cook_book[food_name].append({'ingredient_name':0, 'quantity':0, 'measure':0})
            text.readline()

    return(cook_book)


print(file_opener(file_name))

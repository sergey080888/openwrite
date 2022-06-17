file_name = 'recipes.txt'
def file_opener(file_name):
    with open(file_name) as text:
        data = text.read()
        print(data)


file_opener(file_name)
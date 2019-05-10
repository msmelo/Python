import csv

file_location = ('C:/Users/julia/Documents/Python/Livro/List/List.csv')

with open(file_location) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)

    for row in csv_reader:
        classification, name, ingredients, observation = row
        print(classification, name, ingredients, observation)

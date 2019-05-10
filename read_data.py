import csv

csv_file = open ('applications.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
next(csv_reader)

for row in csv_reader:
    name, email, accepted, coach, language = row
    print(name, email, accepted, coach, language)

csv_file.close()

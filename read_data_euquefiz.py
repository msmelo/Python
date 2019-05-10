import os

path_to_file = 'C:/Users/julia/Documents/Python/applications.csv'
file_exists = os.path.exists(path_to_file)
if file_exists:
    print('The file exists!')
    super_file = open(path_to_file)
    for line in super_file:
        print(line)

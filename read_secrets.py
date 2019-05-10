import os

check_file = True
path_to_file = "C:/Users/julia/Documents/Python/secret.txt"

while check_file:
        file_exists = os.path.exists(path_to_file)
        if file_exists:
            print("secret.txt file exists")
            secret_file = open(path_to_file, 'r+')
            for line in secret_file:
                print(line)

            secret_file.write('I know your secrets.')
            secret_file.close()

            check_file = False

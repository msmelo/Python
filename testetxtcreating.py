import os


path_to_file = "C:/Users/julia/Documents/Python/Olai.txt"

secret_file = open(path_to_file, 'w+')
entrada = input("Escreva o que quiser: ")
print(entrada)
secret_file.write(entrada)
for line in secret_file:
    print(line)
secret_file.close()

def area(side):
    try:
        side= float(side)
        print(side * side)
    except ValueError:
        print("This is not a correct number. Try to run the program again")

side = input("Provide length of a square side: ")
area(side)

def conversion(inches):
    try:
        inches = float(inches)
        print ("The value " + str(inches) + " inches is ecquivalent to " + str(inches * 2.54) + " centimeters.")
    except ValueError:
        print('This is not a correct number. Please run the program again.')
inches = input('Provide number in inches: ')
conversion(inches)

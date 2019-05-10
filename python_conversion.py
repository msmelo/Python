def conversion(inches):
    try:
        inches = float(inches)
        print ("The value " + str(inches) + " inches is ecquivalent to " + str(inches * 2.54) + " centimeters.")
    except ValueError:
        print('This is not a correct number. Please run the program again.')
def conv(cm):
    try:
        cm = float(cm)
        print ("The value " + str(cm) + " centimeters is ecquivalent to " + str(cm / 2.54) + " inches.")
    except ValueError:
        print('This is not a correct number. Please run the program again.')
decision = input("Define your type of conversion: (1:in to cm 2:cm to in)  > ")
decision = float(decision)
if decision == 1:
    inches = input('Provide number in inches: ')
    conversion(inches)
if decision == 2:
    cm = input('Provide number in cm: ')
    conv(cm)

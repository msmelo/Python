#inches = input("Provide number of inches >>> ")
#cm = float(inches)*2.54
#print (inches + " inches is " + str(cm) + " centimeters.")
from Functions.solutionex1_functions import convert_inches

convert_inches(
    "Provide number of inches >>> ",
    "{} inches is {} centimeters",
    "It is not a correct number."
)

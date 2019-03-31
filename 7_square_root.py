# Problem: Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# Import square root function from math module.
from math import sqrt

# Import getFloat function from pcinput.py to ensure input is a positive floating point number. 
from pcinput import getFloat

# Prompt user to enter a positive floating point number and set value to variable i.
i = getFloat("Please enter a positive number: ")

# Format s so there is only 1 decimal place.
s = round(sqrt(i), 1)

# If s is the same as int(s), the number is a whole number square root and not approximate so the output is adjusted.
# Help from https://stackoverflow.com/q/4541155
if s != int(s):
    print("The square root of", i, "is approximately " + str(s) + ".")
else:
    print("The square root of", int(i), "is " + str(int(s)) + ".")
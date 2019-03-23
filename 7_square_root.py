# Problem: Write a program that that takes a positive floating point number as input and outputs an approximation of its square root.

# import square root function from math module
from math import sqrt

# Import getFloat to get user input and set to variable i.
from pcinput import getFloat

i = getFloat("Please enter a positive number: ")

# Formats s so there is only 1 decimal place.
s = round(sqrt(i), 1)

# if s is the same as int(s), the number is a whole number square root and not approximate so the output is adjusted.
# Help from https://stackoverflow.com/q/4541155
if s != int(s):
    print("The square root of", i, "is approximately " + str(s) + ".")
else:
    print("The square root of", int(i), "is " + str(int(s)) + ".")
# Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

# first attempt - see what happens when I just do it the way that seems most straightforward.
# import square root function from math module
# use getFloat from pcinput.py
# format s so there is only 1 decimal place like in example? round()
# how to add full-stop to end like in example? Change s to string format and concatenate.

# should I account for integers with whole number square roots as these answers won't be approximate? 
# to account for this I get help here https://stackoverflow.com/q/4541155
# if s is the same as int(s), the number is a whole number square root and not approximate so the output is adjusted.

from math import sqrt

from pcinput import getFloat

i = getFloat("Please enter a positive number: ")

while i < 0:
    print("That is not a positive number -- please try again.")
    i = getFloat("Please enter a positive number: ")

s = round(sqrt(i), 1)

if s != int(s):
    print("The square root of", i, "is approximately " + str(s) + ".")
else:
    print("The square root of", int(i), "is " + str(int(s)) + ".")    


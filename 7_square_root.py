# Write a program that that takes a positive floating point number as input and outputs
# an approximation of its square root.

# first attempt - see what happens when I just do it the way that seems most straightforward.
# import square root function from math module
# add float before input
# format s so there is only 1 decimal place like in example? round()
# how to add full-stop to end like in example? Change s to string format and concatenate.
# should I account for integers with exact square roots as these answers won't be approximate? 

from math import sqrt

i = float(input("Please enter a number: "))

s = round(sqrt(i), 1)
print("The square root of", i, "is approximately " + str(s) + ".")
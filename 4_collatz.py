# Problem: 
# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation: 
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

# Import getInteger to get user input and set to variable i.
from pcinput import getInteger

i = getInteger("Please enter a positive integer: ")

# i added to list num_list, which will contain the sequence of numbers for the final output.
num_list = [i]

# Collatz conjecture states that any series of numbers created from the 2 calculations will end in 1, no matter the value of i
# Thus the while loop is set to end when it reaches 1.
while i > 1:
    if i % 2 == 0:              # even number
        i = i/2                 # divide by 2         
        num_list.append(int(i)) # add to list - int to remove decimal
    else:            # odd number
        i = (i * 3) + 1         # multiply by 3 and add 1
        num_list.append(int(i)) # add to list - int to remove decimal

# To allow the numbers to print as shown in the example answer, i.e. in a row without the brackets and commas of a printed list 
# Used a variation of the following answer from stack overflow: https://stackoverflow.com/a/17757544
# Only the asterisk operator is needed - removes brackets and commas
print (*num_list)
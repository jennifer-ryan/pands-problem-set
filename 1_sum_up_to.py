# Problem: Write a program that asks the user to input any positive integer and outputs the sum of all numbers between one and that number.

# Import getInteger function from pcinput.py to ensure input is an integer. Set value to variable i.
from pcinput import getInteger

i = getInteger("Please enter a positive integer: ")

# getInteger does not check for negative numbers. i needs to be a positive integer only.
# Using a while loop that only breaks when a positive integer is entered.
# Help from https://stackoverflow.com/a/39855435
while i < 0:
    print("That is not a positive integer -- please try again.")
    i = getInteger("Please enter a positive integer: ")

# Using a for loop to get the sum of numbers.
# Need range from 1 to i + 1 in order to include the user input as the range() function takes you up to but does not include the second number.
# Set variable answer to zero then work through each iteration, adding to answer at end of each loop
# 0 + 1 - answer becomes 1
# 1 + 2 - answer becomes 3
# 3 + 3 - answer becomes 6.....
answer = 0
for num in range(1, i + 1):
    answer += num
    
# print answer to console.
print(answer) 
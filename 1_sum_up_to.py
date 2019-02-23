# Write a program that asks the user to input any positive integer outputs the sum of all numbers between one and that number.

# import getInteger function from pcinput.py to ensure input is an integer. Set value to variable i.
from pcinput import getInteger

i = getInteger("Please enter a positive integer: ")

# getInteger does not check for negative numbers. i needs to be a positive integer only.
# A while loop that only breaks when a positive int is entered? 
# got help from https://stackoverflow.com/questions/39855326/how-to-ask-a-string-again-if-the-wrong-answer-is-entered)
# asks user to input again if number is negative. 
# Is it bad code to have a second input prompt rather than trying to start the program again?
while i < 1:
    print("That is not a positive integer. Please try again.")
    i = getInteger("Please enter a positive integer: ")


# Using a for loop
# need range from 1 to i + 1 in order to include the user input as the range() function takes you up to but does not include the second number.
# set variable answer to zero then work through each iteration, adding to answer at end of each loop
# 0 + 1 - answer becomes 1
# 1 + 2 - answer becomes 3
# 3 + 3 - answer becomes 6
# 6 + 4 - answer becomes 10 .....

answer = 0
for num in range(1, i + 1):
    answer += num
    
# print answer to console.
print(answer)
    

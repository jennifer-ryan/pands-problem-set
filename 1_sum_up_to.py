# Write a program that asks the user to input any positive integer
# and outputs the sum of all numbers between one and that number.

# First attempt. Coding help from "Coder's Apprentice"
# Should I go backwards  with a while loop like in week 4's video? My code seems to work the way it is but is it the best way?

# Ask user for input
# Ensure it is not a float or a string. 
# IF/ELSE? <- does not work
# if type(i) = str or float? <- does not work (ValueError)
# A while loop that only breaks when a positive int is entered? (see https://stackoverflow.com/questions/39855326/how-to-ask-a-string-again-if-the-wrong-answer-is-entered)
# keep getting ValueErrors for the above attempts

# is it possible to use a module for this such as pcinput.py from coders apprentice? Input is required for several of the problems.
# try exception handling to manage float/string input 
# I can get the below to work for the first wrong input (string or float) but get a ValueError for the second wrong input (unless it's a negative integer)
# 
try: 
    i = int(input("Please enter a positive integer: "))
except ValueError:
    print("That is not an integer. Please try again.")
    i = int(input("Please enter a positive integer: "))

# ensure i is a positive integer only (not a negative integer)
if i < 0:
    print("That is not a positive integer. Please try again.")
    i = int(input("Please enter a positive integer: "))


# Trying with a for loop
# need i + 1 to include the user input as a range() function takes you up to but does not include the second number
# start with answer as zero then work through each iteration
# 0 + 1 - answer becomes 1
# 1 + 2 - answer becomes 3
# 3 + 3 - answer becomes 6
# 6 + 4 - answer becomes 10 .....

answer = 0
for num in range(1, i + 1):
    answer += num
    

print(answer)
    

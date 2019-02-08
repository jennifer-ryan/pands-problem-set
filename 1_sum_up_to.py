# Write a program that asks the user to input any positive integer
# and outputs the sum of all numbers between one and that number.

# First attempt. Coding help from "Coder's Apprentice"

# Ask user for input
i = int(input("Please enter a positive integer: "))

# ensure i is a positive integer only (not a negative integer, a float or a string)
# FIGURE THIS OUT. 
# IF/ELSE? 
# .isnumeric? .isalpha?g
# if type(i) = str or float? 

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
    
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

# Prime numbers greater than 1 whose only factors are 1 and itself. 
# a for loop with modulo that tests all numbers (range()) from 2 up to but not including the user input

# First attempt - does not work. Goes through each number and checks whether it is a divisor of i. 
# Prints a line for each number in the range

# second attempt - for a prime number I want the modulo of every number between 2 and i-1 divided into i to never be 0
# separate output when i is 1 or less than 1. Program ends if 1 or a number less than that is entered
# created variable not_prime to have a number added whever the modulo is 0
# after the for loop is complete, if not_prime is greater than 0, that means a divisor has been found that is not 1 or i and the number is not prime
# if not_prime remains at zero, the number is prime


from pcinput import getInteger

i = getInteger("Please enter a positive integer: ")


# still don't know how to restart the program in number less than 1 is entered - tried to reuse the while loops from previous exercises
# but if 1 is entered after 0, it does not revisit previous loop and returns 1 as a prime number 
# Just use one while loop with an if statement within?
# mathematically a prime number is a number greater than 1. 1 itself is not a prime number. Output such and end the program
# if i is less than 1 - prompt user again
while i <= 1:
    if i == 1:
        print("This is not a prime number.")
        exit()
    else:
        print("That is not a positive integer -- please try again.")
        i = getInteger("Please enter a positive integer: ")


not_prime = 0

for number in range(2, i):
    if i % number == 0:
        not_prime += 1

if not_prime > 0:
    print("This is not a prime number.")
else:
    print("This is a prime number.")                
   


# Problem: Write a program that asks the user to input a positive integer and tells the user whether or not the number is a prime.
# Prime numbers: Greater than 1. Only factors are 1 and itself. 

# Import getInteger to get user input and set to variable i.
from pcinput import getInteger

i = getInteger("Please enter a positive integer: ")

# Ensure i is both greater than 1 and positive.
while i <= 1:
    if i == 1: # mathematically 1 itself is not a prime number. Output such and end the program.
        print("This is not a prime number.") 
        exit()
    else:
        print("That is not a positive integer -- please try again.")
        i = getInteger("Please enter a positive integer: ")

# Variable not_prime created to have a number added to it whenever the modulo of the for loop is 0.
not_prime = 0

# For a prime number, the modulo of every number between 2 and i-1 divided into i should never be 0.
for number in range(2, i):
    if i % number == 0:
        not_prime += 1  # if number is a divisor, 1 is added to not_prime.

# If not_prime is greater than 0, that means a divisor has been found that is not 1 or i and therefore the number is not prime.
if not_prime > 0:
    print("This is not a prime number.")
# If not_prime remains at zero, the number is prime.
else:
    print("This is a prime number.")
# Write a program that asks the user to input a positive integer and tells the user
# whether or not the number is a prime.

# Prime numbers only factors are 1 and itself. 
# a for loop with modulo that tests all numbers (range()) from 2 up to but not including the user input

# First attempt - does not work. Goes through each number and checks whether it is a divisor of i.
i = int(input("Please enter a positive integer: "))

for number in range(2, i):
    if i % number > 0:
        print("This is a prime number")
    else:
        print("This is not a prime number")    


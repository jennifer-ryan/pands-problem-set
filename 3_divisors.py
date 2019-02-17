# Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

# range() up to 10001 to include 10000

# for loop with modulo 
# Two conditions need to be true for each number:
# 1. The remainder when divided by 6 must be zero
# 2. The remainder when divided by 12 must not be zero (i.e should be greater than zero) 


for i in range(1000, 10001):
    if (i % 6 == 0) and (i % 12 > 0):
        print(i)
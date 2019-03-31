# Problem: Write a program that prints all numbers between 1,000 and 10,000 that are divisible by 6 but not 12.

# for loop to iterate through each number 
# range() up to 10001 to include 10000. 
for i in range(1000, 10001):
    # if statement and modulo to determine divisors.
    # Two conditions need to be true for each number:
    # 1. When divided by 6 the remainder must be zero.
    # 2. When divided by 12 the remainder must not be zero (i.e should be greater than zero). 
    if (i % 6 == 0) and (i % 12 > 0):
        # print these divisors to console.    
        print(i)
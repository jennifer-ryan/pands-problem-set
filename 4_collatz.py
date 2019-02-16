# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

# First attempt:
# Will just using "while i > 1" suffice to stop the code at 1?
# if loop for each condition
# Need to print i to show first number
# Need to add int before printing i each time to get rid of decimal point
# Results printing one on top of the other unlike example output - SHOULD I MAKE THIS A LIST?
# Still need to test for input other than an integer!


i = int(input("Please enter a positive integer: "))
print(i)

while i > 1:
    if i % 2 == 0:
        i = i/2
        print(int(i))
    elif i % 2 == 1:
        i = (i * 3) + 1
        print(int(i))


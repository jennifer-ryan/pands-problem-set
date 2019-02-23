# Write a program that asks the user to input any positive integer and outputs the successive values of the following calculation. 
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, 
# but if it is odd, multiply it by three and add one. 
# Have the program end if the current value is one.

# First attempt:
# Will just using "while i > 1" suffice to stop the code at 1? - was not aware of collatz conjecture until Skype chat 20.02.19. Since the sequence will always end at one, this while function should suffice.
# if loop for each condition
# Need to print i to show first number
# Need to add int before printing i each time to get rid of decimal point
# Results printing one on top of the other unlike example output - SHOULD I MAKE THIS A LIST? str() does not work.
# Still need to test for input other than an integer!


i = int(input("Please enter a positive integer: "))
num_list = [i]

while i > 1:
    if i % 2 == 0:
        i = i/2
        num_list.append(int(i))
    elif i % 2 == 1:
        i = (i * 3) + 1
        num_list.append(int(i))


# To allow the numbers to print as shown in the example answer 
# i.e. in a row without the brackets and commas of a printed list 
# I used a variation of the following answer from stack overflow: https://stackoverflow.com/a/17757544
# Only the asterisk operator is needed
print (*num_list)
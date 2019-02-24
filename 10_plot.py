# Write a program that displays a plot of the functions x, x**2 and 2**x in the range [0, 4].

# My maths aren't great...
# Assuming x will be the numbers within the range?
# Trying matplotlib tutorial https://matplotlib.org/users/pyplot_tutorial.html



# example from https://stackoverflow.com/a/46726953 adjusted below.
# is this what the problem is looking for?
# Outputs 3 different lines of the graph
import matplotlib.pyplot as plt
# x values
x_values = [0, 1, 2, 3]

# x ** 2 values
x2_values = [0, 1, 4, 9]

# 2 ** x values
x3_values = [1, 2, 4, 8]


# no y values given so this uses the range of the length of each variable as the y functions
plt.plot(x_values, range(len(x_values)))
plt.plot(x2_values, range(len(x2_values)))
plt.plot(x3_values, range(len(x3_values)))
plt.show()

# Write a program that displays a plot of the functions x, x**2 and 2**x in the range [0, 4].

# Matplotlib tutorial https://matplotlib.org/users/pyplot_tutorial.html  
# Help from this example: https://stackoverflow.com/a/46726953 
# y = f(x) https://www.youtube.com/watch?v=2-dUHLHeyTY so y values will be each function (x, x**2 and 2**x) 

# import matplotlib in order to produce a graph.
import matplotlib.pyplot as plt

# x values
x = [0, 1, 2, 3, 4]

# First function is the same as x.
y1 = x

# Using a for loop to get each function for below y list values.
# Second function is x**2.
y2 = []
for i in x:
    i = i ** 2
    y2.append(i)

# Third function is 2**x.
y3 = []
for i in x:
    i = 2 ** i
    y3.append(i)

# Building plots below.
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# To display the graph.
plt.show()
# Outputs the 3 different plotlines on one graph.
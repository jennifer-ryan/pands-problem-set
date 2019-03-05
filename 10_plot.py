# Write a program that displays a plot of the functions x, x**2 and 2**x in the range [0, 4].

# Matplotlib tutorial https://matplotlib.org/users/pyplot_tutorial.html
# plt.plot(x values, y values)
# x values are range[0, 4] - does this want me to include no. 4? range is within square (list) brackets rather than parentheses so I will include no. 4.  
# # y = f(x) https://www.youtube.com/watch?v=2-dUHLHeyTY so y values will be each function (x, x**2 and 2**x) 

# help from this example: https://stackoverflow.com/a/46726953 

# import matplotlib in order to produce a graph.
import matplotlib.pyplot as plt
# x values
x = [0, 1, 2, 3, 4]

# first function is the same as x
y1 = x

# using a for loop to get each function for below y list values
# second function is x**2
y2 = []
for i in x:
    i = i ** 2
    y2.append(i)

# third function is 2**x
y3 = []
for i in x:
    i = 2 ** i
    y3.append(i)

# building plots below
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

# to display the graph
plt.show()
# outputs the 3 different plotlines on one graph.
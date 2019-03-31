# Problem: Write a program that reads in a text file and outputs every second line. The program should take the filename from an argument on the command line.

# Help from this video https://www.youtube.com/watch?v=qjdeQ83T9sQ and this stack overflow question https://stackoverflow.com/a/42040147

# daffodils.txt is in the repository for testing purposes. 

# Required to get filename from an argument on the command line so import sys to use sys.argv
import sys

# Open the file located at index 1 in sys.argv.
# Works with files in the same folder as well as paths.
# Note: since space is the delimiter for command line arguments, the path needs to be enclosed in quotes if it contains spaces https://stackoverflow.com/a/37718627
with open(sys.argv[1]) as f: # with keyword automatically closes file when the program ends.

    # Using .readlines() method to access individual lines https://stackoverflow.com/a/42040147
    # It creates a list with each line as a separate item on the list
    lines = f.readlines()

    # If variable lines is printed at this stage, it comes up as a list with blank lines shown as '\n'
    # below removes the blanks
    for l in lines:
        if l == '\n':
            lines.remove(l)

    # for loop - range starts at 0, ends with the number of lines in the text and does it in increments of 2.
    # i represets the index of each line in lines and every second one should print to console
    for i in range(0, len(lines), 2):
        print (lines[i])
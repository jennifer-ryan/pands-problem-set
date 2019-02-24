# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# Help from this video https://www.youtube.com/watch?v=qjdeQ83T9sQ 
# and this stack overflow question https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python
# https://stackoverflow.com/questions/42040072/how-do-i-read-selected-lines-from-a-text-file-with-python
# Starting by learning how to open a text file


# user will need to input path to file if it is not located in same folder they are running the code from. 
# Below will be string user input eventually
txt_file = "C:\\Users\\Jennifer Ryan\\Desktop\\Daffodils.txt"

# how to open a file
f = open(txt_file, "r+")

# using .readlines() method to access lines https://stackoverflow.com/a/42040147
# looks like it creates a list with each line as a separate item on the list
# indexing to get every second line? 
lines = f.readlines()

# for loop - range starts at 1, ends with the number of lines in the text and does it in increments of 2.
# Does not start at first line though
# i is the index of each line in lines and every second one should print to console
# prints every second line but does not start at first line and also counts blank lines.
for i in range(1, len(lines), 2):
    print (lines[i])

# holding the below - may not be needed
# text = open_file.read()
# print(lines)


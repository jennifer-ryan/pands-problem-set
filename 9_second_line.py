# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# Help from this video https://www.youtube.com/watch?v=qjdeQ83T9sQ 
# and this stack overflow question https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python
# https://stackoverflow.com/questions/42040072/how-do-i-read-selected-lines-from-a-text-file-with-python
# Starting by learning how to open a text file


# user will need to input path to file if it is not located in same folder they are running the code from. 
# Below will be string user input eventually. Currently only works with file in same folder 
# daffodils.txt added to folder
          
txt_file = input("Please enter a text file name: ")

# open the file
f = open(txt_file)

# using .readlines() method to access lines https://stackoverflow.com/a/42040147
# looks like it creates a list with each line as a separate item on the list
# indexing to get every second line? 
lines = f.readlines()

# if I print lines at this stage, it comes up as a list with blank lines shown as '\n'
# maybe I can just remove these from the list?
# it works!
for l in lines:
    if l == '\n':
        lines.remove(l)

# for loop - range starts at 0, ends with the number of lines in the text and does it in increments of 2.
# Does not start at first line though - does if I start the range at 0
# i is the index of each line in lines and every second one should print to console
# prints every second line but does not start at first line and also counts blank lines - problem solved
for i in range(0, len(lines), 2):
    print (lines[i])

#close the  file
f.close()
 

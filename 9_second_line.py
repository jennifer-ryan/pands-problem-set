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
open_file = open(txt_file, "r+")

text = open_file.read()

print(text)


# Write a program that reads in a text file and outputs every second line. 
# The program should take the filename from an argument on the command line.


# Help from this video https://www.youtube.com/watch?v=qjdeQ83T9sQ 
# and this stack overflow question https://stackoverflow.com/questions/32470543/open-file-in-another-directory-python
# https://stackoverflow.com/questions/42040072/how-do-i-read-selected-lines-from-a-text-file-with-python
# Starting by learning how to open a text file


# user will need to input path to file if it is not located in same folder they are running the code from. 
# Below will be string user input eventually
txt_file = "C:\\Users\\Jennifer Ryan\\Desktop\\Daffodils.txt"

# how to open a file using help from https://stackoverflow.com/a/40647980 / https://cmdlinetips.com/2018/01/3-ways-to-read-a-file-and-skip-initial-comments-in-python/ to get rid of empty lines
# does not work. lines is not a list or a string? Needs keyboard interrupt.
with open(txt_file, "r+") as f:
    while True:
        lines = f.readlines()
        for l in lines:
            if not l.startswith("    "):
                break
            else:
                for i in range(1, len(lines), 2):
                    print (lines[i])
            


# using .readlines() method to access lines https://stackoverflow.com/a/42040147
# looks like it creates a list with each line as a separate item on the list
# indexing to get every second line? 


# for loop - range starts at 1, ends with the number of lines in the text and does it in increments of 2.
# Does not start at first line though
# i is the index of each line in lines and every second one should print to console
# prints every second line but does not start at first line and also counts blank lines - help from https://stackoverflow.com/a/40647980.


# holding the below - may not be needed
# text = open_file.read()
# print(lines)


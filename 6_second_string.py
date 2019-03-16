# Problem: Write a program that takes a user input string and outputs every second word.


# To account for punctuation, try to create a for loop that goes through each character in string_sentence and checks for punctuation with the string.punctuation constant (import string first)
# Rather than removing punctuation, it might be better to check for characters not in string.punctuation and creating a final sentence <- it works!

import string # To use string.punctuation at the end.

# Import getString from pcinput.py.
from pcinput import getString

# Prompt user to enter a string and save under the variable sentence. 
sentence = getString("Please enter a sentence: ")

# Breaks sentence into a list of words that can be iterated through.
words = sentence.split()

list_sentence = [] # List will save every second word in words
index = 0 # mimics iterating through the index of words
for w in words:
    if index % 2 == 0: # returns indexes 0, 2, 4, 6, etc.
        list_sentence.append(w) # adds word to new list
    index += 1 # moves on to the next index

# Creates a string from list_sentence separated by a space
string_sentence = " ".join(list_sentence)

# Variable for final output
final_sentence = ""

# Iterates through each character to get rid of punctuation 
for x in string_sentence:
    if x not in string.punctuation:
        final_sentence += x 

# print to console
print(final_sentence)
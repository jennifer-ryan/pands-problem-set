# Problem: Write a program that takes a user input string and outputs every second word.

import re # will be used to remove punctuation for final output

# Import getString from pcinput.py.
from pcinput import getString

# Prompt user to enter a string and save under the variable sentence. 
sentence = getString("Please enter a sentence: ")

# Breaks sentence into a list of words that can be iterated through.
words = sentence.split()

list_second = [] # this list will save every second word in words
index = 0 # mimics iterating through the index of words
for w in words:
    if index % 2 == 0: # returns indexes 0, 2, 4, 6, etc.
        list_second.append(w) # adds every second word to new list
    index += 1 # moves on to the next index

# Create a string from list_second separated by a space
string_sentence = " ".join(list_second)

# Output will print words including punctuation as part of the word 
# Should be no punctuation except for apostrophes that are part of some words (they're, we're, etc.)
# Initially tried string.punctuation but could not exclude apostrophes from being removed
# Search and replace. re.sub help from https://stackoverflow.com/a/47561619
# The character ^ indicates that what follows should not be replaced, i.e.uppercase and lowercase letters, apostrophes and spaces. 
# All other punctuation is replaced with nothing ''
final_sentence = re.sub("[^a-zA-Z' ]", '', string_sentence) 

# print to console
print(final_sentence)
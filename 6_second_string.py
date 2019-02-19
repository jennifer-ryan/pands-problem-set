# Write a program that takes a user input string and outputs every second word.

# The example starts from first word so I will do the same.

# Possible to index each word by dividing the sentence according to the space between them?
# Can use the .split() function for this. If no parameter entered, whitespace is used by default
# .split() creates a list of words that can be iterated through (list_sentence)
# Use a for loop and modulo to iterate through the list. I want indexes 0, 2, 4, 6, etc. 
# If the modulo of the index is 0, amend list_sentence to add each word - this returns every second word and leaves out every word with an index that has a modulo >0.
# This returns a list, but I need a string. Could this be fixed by simply adding str() when printing? <- Doesn't work - still prints a list
# Use the .join() method instead - this is the opposite of .split(). Separate each item on the list by a space(" ") to create a string (string_sentence).
# To account for punctuation, try to create a for loop that goes through each character in string_sentence and checks for punctuation with the string.punctuation constant (import string first)
# Rather than removing punctuation, it might be better to check for characters not in string.punctuation and creating a final sentence <- it works!

import string

sentence = input("Please enter a sentence: ")

words = sentence.split()

list_sentence = []

index = 0

for w in words:
    if index % 2 == 0:
        list_sentence.append(w)
    index += 1


string_sentence = " ".join(list_sentence)

final_sentence = ""

for x in string_sentence:
    if x not in string.punctuation:
        final_sentence += x


print(final_sentence)
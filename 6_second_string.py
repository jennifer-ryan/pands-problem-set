# Write a program that takes a user input string and outputs every second word.
#example starts from first word so I will do the same

# Possible to index each word by dividing the sentence according to the space between them?
# can use the split() functions for this. If no parameter entered, whitespace is used
# does not account for punctuation, which will be considered part of the word - need to figure this out (check out string.punctuation constant)
# split() should create a list of words that can be iterated through
# use a for loop and modulo. I want indexes 0, 2, 4, 6, etc. if modulo is 0, amend the new sentence with the words
# List prints but could it be fixed by simply adding str() when printing? Doesn't work
# use the .join() method instead. Separate each item on the list by a space(" ") to create a string

sentence = input("Please enter a sentence: ")

words = sentence.split()

new_sentence = []

index = 0

for w in words:
    if index % 2 == 0:
        new_sentence.append(w)
    index += 1

output = " ".join(new_sentence)

print(output)


# Trying problem 8 again with a simpler method using strftime

# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm". %-d %Y %-I %-M %p

import datetime as dt 

# Using # instead of - for windows formatting https://stackoverflow.com/a/2073189
print(dt.datetime.strftime(dt.datetime.now(), "%A, %B %#d %Y at %#I:%M%p"))


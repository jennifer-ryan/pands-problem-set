# Trying problem 8 again with a simpler method using strftime

# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm". %-d %Y %-I %-M %p

import datetime as dt 

# function created from original datetime solution
def suffix():
    date = dt.datetime.today().day
    suf = ""

    if date == 1 or date == 21 or date == 31:
        suf = "st"  
    elif date == 2 or date == 22:
        suf = "nd"
    elif date == 3 or date == 23:
        suf = "rd"
    else:
        suf = "th" 
    return suf     


# Using # instead of - for windows formatting https://stackoverflow.com/a/2073189
# broken into 2 variables to add correct suffix in the middle
first = dt.datetime.strftime(dt.datetime.now(), "%A, %B %#d") 
second = dt.datetime.strftime(dt.datetime.now(),"%Y at %#I:%M%p")

print (first+suffix(), second)

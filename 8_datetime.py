# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm".

# testing out datetime module
# datetime.now() prints year-month-day-time
# should I create functions for each part? tried on first commit
# maybe I don't need functions

from datetime import datetime

# Day. On datetime 0 = Monday, 1 = Tuesday, 2 = Wednesday, etc. 
# Converted each number to a string in variable d.
day = datetime.today().weekday()
d = ""

if day == 0:
    d = "Monday"
elif day == 1:
    d = "Tuesday"
elif day == 2:
    d = "Wednesday"
elif day == 3:
    d = "Thursday"
elif day == 4:
    d = "Friday"
elif day == 5:
    d = "Saturday"
elif day == 6:
    d = "Sunday"                    


# Month. Same technique as above. 
month = datetime.today().month  
m = ""

if month == 1:
    m = "January"
elif month == 2:
    m = "February"
elif month == 3:
    m = "March"    
elif month == 4:
    m = "April"
elif month == 5:
    m = "May"
elif month == 6:
    m = "June"
elif month == 7:
    m = "July"
elif month == 8:
    m = "August"
elif month == 9:
    m = "September"
elif month == 10:
    m = "October"
elif month == 11:
    m = "November"
elif month == 12:
    m = "December"


# started with a lot of elif statements like above but changed it to a for loop with a range to cover all dates - unecessary. if/elif should suffice
# concatenated dates with suffixes 
# suffixes st (for 1, 21 and 31), nd (for 2 and 22), and rd (for 3 and 23) dealt with first.
# all others should (hopefully) fall into the else statement containing th
date = datetime.today().day
dte = ""

if date == 1 or date == 21 or date == 31:
    dte = str(date) + "st"
elif date == 2 or date == 22:
    dte = str(date) + "nd"
elif date == 3 or date == 23:
    dte = str(date) + "rd"
else:
    dte = str(date) + "th"             

# Year
year = datetime.today().year

# Hour - 12 hour clock
# example does not use 24hr clock - check modules for am/pm options
# changed for loop to if/else it wasn't working for a.m.
hour = datetime.today().hour
hr = ""

if hour in range(13, 24):
    hr = hour - 12
else: 
    hr = hour

# Minute
# just realised single digit minutes print as 3:5 instead of 3:05
# added an if statement to concatenate 0 to minutes under 10.
minute = datetime.today().minute
min = str(minute)

if minute in range(0, 10):
    min = "0" + min

# To add a.m. or p.m. to the end of the string.
# Between the hours of 00:00 to 11:59, it should add a.m. All other times should add p.m. 
# Need to test this at different times
# transition from am to pm works. Need to check pm to am

if hour in range(0, 12):
    min += "am"
else:
    min += "pm"


print(d + ", " + m, dte, year, "at", str(hr) + ":" + min)
# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm".

# testing out datetime module
# datetime.now() prints year-month-day-time
# should I create functions for each part? tried on first commit
# maybe I don't need functions
# day and month done. Is there an easier way though??

from datetime import datetime

# Day. On datetime 0 = Monday, 1 = Tuesday, 2 = Wednesday, etc. 
# Converted each to a string in variable d and added comma
day = datetime.today().weekday()
d = ""

if day == 0:
    d = "Monday,"
elif day == 1:
    d = "Tuesday,"
elif day == 2:
    d = "Wednesday,"
elif day == 3:
    d = "Thursday,"
elif day == 4:
    d = "Friday,"
elif day == 5:
    d = "Saturday,"
elif day == 6:
    d = "Sunday,"                    


# Month. Same technique as above. Can't figure out a more efficient way of doing this.
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


# started with a lot of elif statements like above but changed it to a for loop with a range to cover all dates.
# concatenated dates with suffixes 
# suffixes st (for 1, 21 and 31), nd (for 2 and 22), and rd (for 3 and 23) dealt with first.
# all others should (hopefully) fall into the else statement containing th
date = datetime.today().day
dte = ""

for x in range(1, 32):
    x = date
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
hour = datetime.today().hour
hr = ""

for h in range(13, 24):
    h = hour
    hr = h - 12

# Minute
minute = datetime.today().minute

# To add a.m. or p.m. to the end of the string.
# create variable min, which convert minute to string format 
# Between the hours of 00:00 to 11:59, it should add a.m. All other times should add p.m. 
# Need to test this at different times
min = str(minute)
if hour in range(0, 12):
    min += "a.m."
else:
    min += "p.m."

print(d, m, dte, year, "at", str(hr) + ":" + min)
# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm".

# Import datetime to get access to date and time
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

# Date
# Each date concatenated with appropriate suffixes 
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

# Hour - adjusted as 12 hour clock needed
hour = datetime.today().hour
hr = ""

if hour in range(13, 24):
    hr = hour - 12
else: 
    hr = hour

# Minute
minute = datetime.today().minute
min = str(minute)
# single digit minutes need a 0 prefix
if minute in range(0, 10):
    min = "0" + min     

# Adds am or pm to the end of the string.
if hour in range(0, 12):
    min += "am"
else:
    min += "pm"

# print complete string to console.
print(d + ", " + m, dte, year, "at", str(hr) + ":" + min)
# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm".

# testing out datetime module
# datetime.now() prints year-month-day-time
# should I create functions for each part? tried on first commit
# maybe I don't need functions
# day and month done. Is there an easier way though??

from datetime import datetime

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




print(d, m)
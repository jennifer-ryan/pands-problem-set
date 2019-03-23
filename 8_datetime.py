# Problem: Write a program that outputs today’s date and time in the format "Monday, January 10th 2019 at 1:15pm".
# Note: This is an entirely different version of original code using strftime. 
# Please see old commits for original solution, which worked but was very inefficient.

# Import datetime to get access to date and time
import datetime as dt 

# Broken into 2 variables to add correct suffix for the date in the middle
# first returns day, month, date
first = dt.datetime.strftime(dt.datetime.now(), "%A, %B %#d") # Windows formatting uses '#' instead of '-' https://stackoverflow.com/a/2073189
# second returns year and time
second = dt.datetime.strftime(dt.datetime.now(),"%Y at %#I:%M")

# Function suffix() created from original datetime solution to get suffixes for the date ('st', 'nd', 'rd' or 'th')
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

# Cannot get %p in strftime to print am/pm as lowercase on Windows so wrote function below for this, based on what was written in first solution
def ampm():
    hour = dt.datetime.today().hour
    end = ""
    if hour in range(0, 12):
        end = "am"
    else:
        end = "pm"
    return end    

# Concatenate within print function to print whole string to console
print (first+suffix(), second+ampm())
# Write a program that outputs today’s date and time in the format 
# "Monday, January 10th 2019 at 1:15pm".

# testing out datetime module
# datetime.now() prints year-month-day-time
# should I create functions for each part?
# function day created to get the day, comma and space


from datetime import datetime

def day():
    today = datetime.today().weekday()
    if today == 0:
        print("Monday, ")
    elif today == 1:
        print("Tuesday, ")
    elif today == 2:
        print("Wednesday, ")
    elif today == 3:
        print("Thursday, ")
    elif today == 4:
        print("Friday, ")
    elif today == 5:
        print("Saturday, ")
    elif today == 6:
        print("Sunday, ")                    
    
day()   
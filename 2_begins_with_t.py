# Problem: Write a program that outputs whether or not today is a day that begins with the letter T. 

# Indexing of days in datetime.
# Similar to tuesday.py from week 1 lecture.

# Import datetime module which determines the day of the week.
import datetime

# The only days that begin with T are Tuesday (index 1 in datetime) and Thursday (index 3 in datetime).
# If either are True, print the "Yes..." string.
if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
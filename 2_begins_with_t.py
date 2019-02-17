# Write a program that outputs whether or not today is a day that begins with the letter T. 

# indexing?
# similar to tuesday.py from week 1?
# Only days that begin with T are Tuesday (index 1) and Thursday (index 3)
# So if either are True, print the "Yes..." string


import datetime

if (datetime.datetime.today().weekday() == 1) or (datetime.datetime.today().weekday() == 3):
  print("Yes - today begins with a T.")
else:
  print("No - today does not begin with a T.")
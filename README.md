# Programming and Scripting Problem Set 2019


## Description:
This repository contains my solutions to ten problems that comprise part of my first assessment in Python programming for the Higher Diploma on Data Analytics with Galway-Mayo Institute of Technology. 


## How to Download the Repository:
1. Go to the pands-problem-set repository on [GitHub](https://github.com/jennifer-ryan/pands-problem-set)
2. Click the *clone or download* button. This allows you to use it in GitHub Desktop or download a zip file.


## How to Run the Code:
1. Make sure you have Python installed on your machine. If you do not and are interested in data science, I recommend [Anaconda](https://www.anaconda.com/distribution/) as it contains many packages that work with Python and porting for all popular Python libraries.
2. On the command line, go to the directory that contains the unzipped download for [pands-problem-set](https://github.com/jennifer-ryan/pands-problem-set) or use GitHub Desktop.
3. If using the command line, enter *python* followed by the name of the program you wish to run, e.g. *1_sum_up_to.py*


## External Module Used for User Input:
Many of the problems contained within require the user to enter input, either an integer, float, or string. To ensure that the input entered is of the correct format, I decided to use a module created by Pieter Spronck, author of [The Coder's Apprentice](http://spronck.net/pythonbook/pythonbook.pdf).

This module is called [pcinput.py](http://www.spronck.net/pythonbook/). To download this module, click the link entitled [Listings, library code, exercise templates and test files](http://www.spronck.net/pythonbook/pythonbooklistings.zip) which will download a zip file that contains pcinput.py.

This module contains four functions that ensure the input entered by the user is of the correct data type. For this problem set, I have altered pcinput.py as I only require the first three: getFloat, getInteger and getString. 

The getFloat and getInteger functions work through exception handling, utilising the *try* and *except* clauses. If the user input is of the desired data type, i.e. the *try* portion of the code, then there should be no error that requires the *except* clause to launch. If the user enters input that is incorrect, the subsequent ValueError will trigger the *except clause, which will prompt the user to try again.

The getString function uses the *.strip()* method to remove leading and trailing spaces from the user input.


## Files in this Repository:

### 1_sum_up_to.py
This program asks the user to enter a positive integer and outputs the sum of all numbers between one and that number.
* Import **getInteger** from **pcinput.py**.
* Ask user to enter a positive integer using **getInteger**. Set to variable *i*.
* A **while loop** ensures that *i*  is positive.
* The variable *answer* is created and set to zero.
* A **for loop** is used with a **range() function** to iterate through all numbers between one and the user input, *i*,  adding each number to *answer* until it reaches the last number.
* Once the loop is complete, *answer* is printed.

### 2_begins_with_t.py
This program determines whether today is a day that begins with the letter 'T'.
* Similar to **tuesday.py**, which was part of the Week 1 lecture series. 
* The **datetime** module is imported, allowing the program to determine what day it is when it is run.
* **if/else statements** and the keyword **or** are used. If today is Tuesday (weekday index 1) **or** Thursday (weekday index 3), the output will read "Yes - today begins with a T". Otherwise the output will read "No - today does not begin with T".

### 3_divisors.py
This program prints all numbers between 1,000 and 10,000 that are divisible by 6 but not by 12.
* A **for loop** along with the **modulo operator** are used to iterate through each number in the **range()** provided.
* Two conditions need to be true for this program to work as intended: 
    * The remainder when each number is divided by 6 must be 0.
    * The remainder when each number is divided by 12 must not be 0.
* The keyword **and** is used to ensure both of the above conditions are true.
* The program only prints the numbers that meet both conditions.

### 4_collatz.py
This program asks the user to input any positive integer and outputs the successive values of the following calculation: At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. The program ends when the current value is 1.
* Import **getInteger** from **pcinput.py**.
* Ask user to enter a positive integer using **getInteger**. Set to variable *i*.
* A **while loop** ensures that *i* is positive.
* A **list** is created called *num_list* and variable *i* is stored there. A list will help generate the desired output, i.e. numbers printed in a row rather than as a column.
* The program goes through the required calculation with a **while loop** along with **if/elif statements** and **modulo operators**:
    * The condition in the while loop (while *i* > 1) is based on the collatz conjecture, which states that the sequence of numbers that result from the above calculation will always end at 1, no matter the value of *i*. Thus, once the while loop reaches 1, the program ends.
    * The if statement checks whether the value of *i* is an even number, i.e. the modulo of *i* divided by 2 should be 0. If it is, *i* is divided by 2 and added to *num_list*.
    The elif statement checks whether the value of *i* is an odd number, i.e. the modulo of *i* divided by 2 should be 1. If it is, *i* is multiplied by 3 and 1 is added to it. This number is then added to *num_list*.
    * The final result is printed to the console using the **asterisk operator**, which removes the brackets and commas that are generated when a list is printed.

### 5_primes.py
This program asks the user to input a positive integer and tells the user whether or not the number is a prime.
* Import **getInteger** from **pcinput.py**.
* Ask user to enter a positive integer using **getInteger**. Set to variable *i*.
* A **while loop** along with an **if/else statement** are used to determine whether *i* is 1 (and therefore not a prime number mathematically) or less than 1 (i.e. not a positive integer).
* The variable *not_prime* is created to track the result of the next part of the program.
* A **for loop** is used to iterate through all numbers in the **range()** from 2 to i and checks whether each number in the range divides into i with a remainder or not. If the **modulo** of a division is ever equals to zero, then 1 is added to *not_prime*.
* An **if/else statement** is used to determine the final output. If *not_prime* is greater than zero, that means a divisor other than 1 and itself has been found for the variable *i*, meaning it is not a prime number. Otherwise, the number is prime. The result is printed to the console. 

### 6_second_string.py
This program takes a user input string and returns every second word.
* Import **string** module in order to use the **string.punctuation constant** later in the program.
* Ask user to enter a string and save under variable *sentence*.
* The **.split()** method with no parameter (default is white space) is applied to *sentence*, creating a **list** of the words in *sentence*. This is list is named *words*.
* An empty **list** is created, named *list_sentence*, to store every second item in the *words* list and the variable *index* is created and set to 0, which allows the **for loop** to mimic iterating through each index of the list.
* A **for loop** is used to iterate through every item (*w*) in *words*. The program needs to return the first word (*index* 0 at first iteration) and every second word after that (index 2, 4, 6, etc.). Thus the **modulo operator** is used. If the modulo of *index* divided by 2 is zero, the word is added to *list_sentence* using the **.append()** method. 1 is then added to *index* for the next item.
* *list_sentence* is converted back to a string using the **.join()** method with " " to input white space as the joiner. This is named *string_sentence*.
* *string_sentence* contains punctuation as part of each word. In order to remove punctuation, a **for loop** is used to iterate through each character in *string_sentence*. The **string.punctuation constant** is used to determine whether a character is considered punctuation. If it is not, the character is added to the empty variable *final_sentence*, which is then printed to the console.

### 7_square_root.py
This program asks the user to enter a positive floating number and returns an approximation of the square root.
* Import **sqrt** function from **math** module and **getFloat** function from **pcinput.py** module.
* Ask user to enter a positive number using **getFloat**. Set to variable *i*.
* A **while loop** ensures that *i* is positive.
* The square root of *i* is calculated using the **sqrt()** function and rounded to 1 decimal place using the **round()** function. This is saved under variable *s*.
* In order to account for square roots that are integers rather than floats, there are 2 output options. An **if/else statement** is used to determine whether *s* is the same number as a float and as an integer. If it is, the output prints "The square root if i is s.". Otherwise it prints "The square root of i is approximately s." 

### 8_datetime.py
This program outputs today's date and time in the format: "Sunday, March 3rd 2019 at 1:40pm".
* **datetime** imported from **datetime** to determine today's date. 
* Day: **datetime.today().weekday()** provides the day of the week and this is saved to variable *day*. This encodes each day as a number between 0 and 6. **if/elif statements** are used to convert the weekday number to a string which is saved to variable *d*.
* Month: **datetime.today().month** provides the month and this is saved to variable *month*. This encodes each month as a number between 1 and 12. **if/elif statements** are used to convert the month number to a string which is saved to variable *m*.
* Date: **datetime.today().day** provides the date and this is saved to the variable *date*. In order to get each date with the appropriate suffix for the string (st, nd, rd, th), **if.elif statements** are used wo determine the appropriate suffix for each number. The date is converted to a string and concatenated to the suffix and saved as variable *dte*.
* Year: **datetime.today().year** provides the year directly. This s saved to the variable *year*.
* Hour: **datetime.today().hour** provides the hour portion of the time in 24 hour format and this is saved to the variable *hour*. The output requires 12 hour format so an **if/else statement** is used to convert the hours in the **range()** 13:00 to 23:00 inclusive into 12 hour format by subtracting 12. Hours outside of this range remain unchanged. This is saved as a string in the variable *hr*.0
* Minute: **datetime.today().minute** provides the minutes portion of the time and is saved to the variable *minute*. An **if statement** addresses minutes in the **range() 0 to 9 inclusive and concatenates a zero in front as these are originally returned as single digits. Minutes are saved in string format in the variable *min*. 
* AM/PM: In order to add am and pm to the time, an **if/else statement** is used and if the *hour* portion of the time is in the **range()** 0 to 11 inclusive, the suffix am is concatenated to the *min* variable. Otherwise the suffix pm is concatenated. 
* The final print statement joins all of the variables created and punctuation into a string.  

### 9_second_line.py
This program reads in a text file and outputs every second line.
* The user is asked to enter the name of a text file. This is saved as the variable *txt_file*.
* File is opened using **open()** and saved to the variable *f*.
* To access each individual line, the **readlines()** method is used. This creates a list that contains each line as a separate item in the list, allowing the program to iterate through them later. This list is named *lines*.
* To remove empty lines, a **for loop** iterates through each item in *lines* and an **if statement** removes any blank lines from the list.
* To return every second line of the text file, a **for loop** is used to access the index of every second item in *lines*. The loop iterates through a range from 0 up to the number of items in *lines* in increments of 2. These lines are then printed to the console.
* The file is closed using **close()**.

### 10_plot.py
This program displays a plot of the functions x, x^2 and 2^x in the range [0, 4].
* **matplotlib.pyplot** imported (as plt) to plot and create the graph.
* **List** *x* created with range [0, 4].
* **List** *y1* created and set equal to variable *x*.
* **Lists** *y2* and *y3* created using **for loops** to iterate through each value of x and apply the calculations x^2 and 2^x respectively.
* The function **plt.plot** is used to create each plot using the x values and various y values. 
* The graph is displayed using the function **plt.show()**.

# References
Spronck, P. (2016) [*The Coder's Apprentice*](http://spronck.net/pythonbook/pythonbook.pdf)
* I used this excellent resource to learn the majority of the basic code utilised in this problem set.

[Python 3.7.2 Documentation](https://docs.python.org/3/)
* Used to get a deeper understanding of Python code.

[Stack Overflow](https://stackoverflow.com/)
* Used for more specific help with particular problems.

[YouTube](https://www.youtube.com/)
* Used for various tutorial videos.

https://github.com/ianmcloughlin/python-tuesday
* Used as model for *2_begins_with_t.py*
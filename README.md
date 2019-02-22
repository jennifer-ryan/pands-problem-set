# Programming and Scripting Problem Set 2019


## Description:
This repository contains my solutions to ten problems that comprise part of my first assessment in Python programming for the Higer Diploma on Data Analytics with Galway-Mayo Institute of Technology. 


## How to dowload the repository:
1. Go to my repository on [GitHub](https://github.com/jennifer-ryan/pands-problem-set)
2. Click the *clone or download* button. This allows you to use it in GitHub Desktop or download a zip file.


## How to run the code:
1. Make sure you have Python installed on your machine. If you do not and are interested in data science, I recommend [Anaconda](https://www.anaconda.com/distribution/) as it contains many packages that work with Python and contains porting for all popular Python libraries.
2. On the command line, go to the directory that contains the unzipped download for [pands-problem-set](https://github.com/jennifer-ryan/pands-problem-set) or use GitHub Desktop.
3. If using the command line, enter *python* followed by the name of the program you wish to run, e.g. *1_sum_up_to.py*


## Note on module used for user input:
Many of the problems contained within require the user to enter input, either an integer, float, or string. To ensure that the input entered is of the correct format, I decided to use a module created by Pieter Spronck, author of ][The Coder's Apprentice](http://spronck.net/pythonbook/pythonbook.pdf).

This module is called [pcinput.py](http://www.spronck.net/pythonbook/). To download this module, click the link entitled [Listings, library code, exercise templates and test files](http://www.spronck.net/pythonbook/pythonbooklistings.zip) which will download a zip file that contains pcinput.py.

This module contains four functions that ensure the input entered by the user is of the correct data type. For this problem set, I only use the first three: getFloat, getInteger and getString. These functions work through exception handling, utilising the *try* and *except* clauses. If the user input is of the desired data type, i.e. the *try* portion of the code, then there should be no error that requires the *except* clause to launch. If the user enters input that is incorrect, the ValueError will trigger the *except clause, which will prompt the user to try again.


## Files in this repository:

### 1_sum_up_to.py
This program asks the user to enter a positive integer and outputs the sum of all numbers between one and that number.
* I used the function getInteger from the module pcinput.py to get the user input.
* The variable *answer* is created and set to zero.
* A *for loop* is used to iterate through all numbers between one and the user input, adding each number to *answer* until it reaches the last number.

### 2_begins_with_t.py

### 3_divisors.py

### 4_collatz.py

### 5_primes.py

### 6_second_string.py

### 7_square_root.py

### 8_datetime.py

### 9_second_line.py

### 10_plot.py

# References
Spronck, P. (2016) [*The Coder's Apprentice*](http://spronck.net/pythonbook/pythonbook.pdf)
* I used this excelelnt resource to learn the majority of the basic code utilised in this problem set.

[Python 3.7.2 Documentation](https://docs.python.org/3/)
* Used to get a deeper understanding of Python code.

[Stack Overflow](https://stackoverflow.com/)
* Used for more specific help with particular problems.

https://github.com/ianmcloughlin/python-tuesday
* Used as model for *2_begins_with_t.py*
# pcinput.py is a module created by Pieter Spronck for his book 'The Coder's Apprentice'. 
# Below I have taken three functions from this module which will be used in several of the problems.
# All problems asking the user to input an integer or float require a positive number 
# Thus, I have adjusted the functions getFloat and getInteger so that negative numbers are not accepted as input.  

def getFloat(prompt):
    while True:
        try:
            num = float( input( prompt ) )
            # added if statement below if negative number entered
            if num < 0:
                print ("That is not a positive number - please try again")
                continue
        except ValueError:
            print( "That is not a number -- please try again" )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
            # added if statement below if negative number entered
            if num < 0:
                print ("That is not a positive number - please try again")
                continue
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()



# pcinput.py is a module created by Pieter Spronck for his book 'The Coder's Apprentice'. 
# Below I have taken three functions from this module which will be used in several of the problems.


def getFloat( prompt ):
    while True:
        try:
            num = float( input( prompt ) )
        except ValueError:
            print( "That is not a number -- please try again" )
            continue
        return num

def getInteger( prompt ):
    while True:
        try:
            num = int( input( prompt ) )
        except ValueError:
            print( "That is not an integer -- please try again" )
            continue
        return num

def getString( prompt ):
    line = input( prompt )
    return line.strip()



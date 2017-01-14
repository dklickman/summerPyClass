# bring in the regex
import re

def run(myTuple,myWord):
    print("David Klickman")
    print(myWord)
    print(myTuple)
    throwItBack = list(filter((lambda x: re.search(myWord, x)),myTuple))
    return throwItBack

import re

myTuple = ('Joe is a friend.','Dick is a name.','Tom Dick and Harry.','Joe and Sue.')
myWord = 'Joe'
print("David Klickman")

print(filter((lambda x: re.search(myWord, x)),myTuple))

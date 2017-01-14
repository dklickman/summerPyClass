import re
myTuple = ['Joe is a friend.','Dick is a name.','Tom Dick and Harry.','Joe and Sue.']
myWord = 'Joe'


print(list(filter((lambda x: re.search(myWord, x)),myTuple)))


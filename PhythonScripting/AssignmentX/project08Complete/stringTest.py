myList = ['big','house','fun','ping','ball']
char = 'i'
print(myList)

listB = []

for listCandidate in myList:
    if char not in listCandidate:
        listB.append(listCandidate)


print(listB)

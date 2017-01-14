str = 'The lazy brown fox'
index = 6

print("David Klickman")
print(str)
print(index)


myList = []
myList.append(str[:index])
print(myList)
myList.append(str[index-1:])
print(myList)


# use split([index-1:])

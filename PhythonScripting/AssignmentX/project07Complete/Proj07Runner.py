def run(str,index):

    # Print required info
    print("David Klickman")
    print(str)
    print(index)

    # create an empty list to assign to
    myList = []

    # slice out from the index and from the index - 1
    # appending to myList
    myList.append(str[:index])
    myList.append(str[index-1:])

    return myList

    

    

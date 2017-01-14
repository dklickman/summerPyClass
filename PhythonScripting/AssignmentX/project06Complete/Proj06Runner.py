def run(str,sep):
    
    # print the required information 
    print("David Klickman")
    print(str)
    print(sep)

    # create an empty list for assigning elements
    myList = []

    # loop through str until 'sep' is found, then append
    # to a new element
    for line in str.split(sep):
        myList.append(line)

    return myList
    
    
    
    
   
    

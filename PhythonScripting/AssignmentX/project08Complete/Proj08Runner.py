def run(myListA,char):

    # print the required output 
    print("David Klickman")
    print(char)
    print(myListA)

    # Create an empty list to assign to 
    listB = []

    # iterate through list, if element does not contain
    # 'char' then append to list
    
    for listCandidate in myListA:
        if char not in listCandidate:
            listB.append(listCandidate)

    return listB
        

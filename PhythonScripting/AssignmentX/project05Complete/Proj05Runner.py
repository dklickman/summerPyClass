# Function that receives the two string parameters and manipulates data
def run(str,subStr):

    # assign the parameters to variables and return the search
    full = str
    partial = subStr
    searchResult = findIt(full,partial)

    # add new line charaters to strings
    myName = addNewLine("David Klickman")
    full = addNewLine(full)
    partial = addNewLine(partial)
    

    # concatenate and return
    quickFox = myName+full+partial+searchResult
    return quickFox    

# Finds the subString index and +3,-3 returns the result
def findIt(full,partial):
    
    # This section finds the subString search 
    findIt = full.find(partial)
    findItLen = len(partial)
    findItEnd = findIt + findItLen 
    foundIt = full[findIt:findItEnd]


    # This section finds the head (-3 index places)
    findHead = findIt - 3
    foundHead = full[findHead:findIt]


    # This section finds the tail (+3 index from findItEnd)
    findTail = findItEnd + 3
    foundTail = full[findItEnd:findTail]

    # glue the slices back together and return 
    indexSearch = foundHead+foundIt+foundTail
    return indexSearch

# Adds a newline character to string
def addNewLine(inStr):
    newLineString = inStr + "\n"
    return newLineString

import dbm.dumb

def run(myKeys,myValues,databaseName):
    # print author name 
    print("David Klickman")

    # Create and open the DB
    dumbDB = dbm.dumb.open(databaseName, 'c')

    # Assign the keys and values 
    for index in range(len(myKeys)):
        dumbDB[myKeys[index]]=myValues[index]

    
    
    

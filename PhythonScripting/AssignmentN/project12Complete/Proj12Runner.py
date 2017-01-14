import dbm.dumb

def run(databaseName):
    # print the author's name
    print("David Klickman")

    # create the database file
    dumbDB = dbm.dumb.open(databaseName, 'c')

    # create the DB keys and values
    myKeys = b'name',b'age',b'gender'
    myValues = b'Joe',b'39',b'male'

    # Populate the DB
    for index in range(len(myKeys)):
        dumbDB[myKeys[index]]=myValues[index]
    
    
    




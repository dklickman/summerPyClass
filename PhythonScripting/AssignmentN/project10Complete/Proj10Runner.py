# import the dumb module
import dbm.dumb

def run(myKeys,myValues,databaseName):
    print("David Klickman")

    # open the dumb DB
    dumbDB = dbm.dumb.open(databaseName, 'c')
    
    # loop and assign values to the DB file
    for index in range(len(myKeys)):
        dumbDB[myKeys[index]]=myValues[index]

    # loop and print the key and value 
    for key,value in dumbDB.items():
        print("key: " + str(key) + " value: " + str(value))

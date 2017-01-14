import dbm.dumb

myKeys = b'name',b'age',b'gender'
myValues = b'Joe',b'39',b'male'
databaseName = 'database'


# print author's name
print("David Klickman")

# open the dumb DB
dumbDB = dbm.dumb.open(databaseName, 'c')

# loop and assign values to the DB file
for index in range(len(myKeys)):
    dumbDB[myKeys[index]]=myValues[index]
    

# loop and print the key and value 
for key,value in dumbDB.items():
    print("key: " + str(key) + " value: " + str(value))









      





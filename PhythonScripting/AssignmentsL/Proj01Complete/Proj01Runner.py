# Create a class to extend the Proj01 file
class Runner():


    # This is the only method that is directly called by Proj01
    def run(aTuple):
        # Create a list to store the turtles
        myList = []

        # turtle is awkward to type so they are now turds
        turd1 = aTuple[0]
        turd2 = aTuple[1]
        turd3 = aTuple[2]

        # Fill the list with turds  
        myList.append(turd1)
        myList.append(turd2)
        myList.append(turd3)

        # Add this non-turd last 
        myList.append("David Klickman")

        # add attributes to turd1
        myList[0].color("red")
        myList[0].shape("turtle")

        # add attributes to turd2
        myList[1].pensize(2)
        myList[1].color("green")
        myList[1].shape("circle")
        
        #add attributes to turd3
        myList[2].pensize(3)
        myList[2].color("blue")
        myList[2].shape("arrow")

        return myList

import turtle

def Runner(Color):
    turtleA = turtle.Turtle()
    turtleA.color(Color)
    turtleA.shape("turtle")
    yourName = "David Klickman"
    return turtleA
    
    
    
    
def main():
    objA = Runner("red") #create one object
    objB = Runner("green") #create a second object

    objA.forward(100)
    objB.right(90)
    objB.forward(100)


    #Call the run method on each object and unpack
    # the tuple that is returned.
    #colorA,turtleA,yourName = objA.run()
    #colorB,turtleB,yourName = objB.run()

    window.title(yourName)
main()

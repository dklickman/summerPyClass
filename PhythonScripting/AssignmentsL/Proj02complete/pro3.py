import turtle
# expand pro1 with class Runner
class Runner():

    
     
    def __init__(self, tColor):
        self.thisTurd = turtle.Turtle()
        self.color = tColor
        self.thisTurd.shape("turtle")
        self.thisTurd.pensize(5)
        
    

    # class method that can be called by object
    def run(self):
        color = self.color
        turd = self.thisTurd
        yourName = "David Klickman"
        myTurdTup = (color, turd, yourName)
        return myTurdTup

window = turtle.Screen()
turtle.setup(400,400)

objA = Runner("red")
objB = Runner("green")


colorA,turtleA,yourName = objA.run()
colorB,turtleB,yourName = objB.run()



colorA = objA.color
turtleA = objA.thisTurd
yourName = "David Klickman"

colorB = objB.color
turtleB = objB.thisTurd
yourName = "David Klickman"

window.title(yourName)

turtleA.left(90)
turtleA.stamp()
turtleA.right(90)
turtleA.forward(50)
turtleA.right(30)
turtleA.color(colorA)
turtleA.forward(50)

turtleB.right(180)
turtleB.forward(50)
turtleB.left(30)
turtleB.color(colorB)
turtleB.forward(50)


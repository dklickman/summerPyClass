import turtle

# expand Proj03.py with class Runner
class Runner():

    # initialize the object and assign instance values 
    def __init__(self, tColor):
        self.thisTurd = turtle.Turtle()
        self.color = tColor
        self.thisTurd.pensize(3)
        self.thisTurd.shape("turtle")
        self.addClassVar(tColor)

    # This function called by init will effectively assign color2 to both
    # colorA and colorB when run() occurs 
    def addClassVar(self,tColor):
         Runner.tColor = tColor
        
  
        
    

    # Class method to be called by objA and objB
    def run(self):
        # assigns the class variable Runner.tColor to colorA and colorB
        color = Runner.tColor
        
        turd = self.thisTurd
        yourName = "David Klickman"
        myTurdTup = (color, turd, yourName)
        
        return myTurdTup

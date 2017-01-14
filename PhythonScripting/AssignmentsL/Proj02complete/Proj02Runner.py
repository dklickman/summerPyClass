import turtle

# expand Proj02.py with class Runner
class Runner():
  
    # initialize the object and assign instance values 
    def __init__(self, tColor):
        # create a turd
        self.thisTurd = turtle.Turtle()
        
        # pass the color value into the instance 
        self.color = tColor

        # assign the turd a shape 
        self.thisTurd.shape("turtle")
        
        
    

    # class method that can be called by object
    def run(self):
        color = self.color
        turd = self.thisTurd
        yourName = "David Klickman"
        
        # make a tuple to pass back into Proj02
        myTurdTup = (color, turd, yourName)
        
        return myTurdTup

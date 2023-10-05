# This class defines the snake object which is represented 
# using a linkedlist

class node:
    def __init__(self):
        self.xPos = 0
        self.yPos = 0
        self.heading = None

    def setX(self, inputX):
        self.xPos = inputX

    def setY(self, inputY):
        self.yPos = inputY



class snake:
    def __init__(self):
        xPos = 0
        yPos = 0
        length = 0
        heading = "right"


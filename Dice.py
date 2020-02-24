import random
class Dice:

    
    #Initializes the Dice object with a number of faces, stored as DieSize
    def __init__(self, DieSize):
        self.DieSize = DieSize


    #Rolls the Dice object, returning a value between 1 and the DieSize
    def Roll(self):
        theRoll = random.randrange(1,(self.DieSize+1))
        return theRoll

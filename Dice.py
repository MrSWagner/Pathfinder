import random
class Dice:

    
    #Initializes the Dice object with a number of faces, stored as DieSize
    def __init__(self, DieSize = 12):
        self.DieSize = DieSize


    #Rolls the Dice object, returning a value between 1 and the DieSize
    def Roll(self, numDie = 1):
        i = 0
        theRoll = 0
        while i < numDie:
            if theRoll == 0:
                theRoll = random.randrange(1,(self.DieSize+1))
            else:
                theRoll += random.randrange(1,(self.DieSize+1))
            i += 1
        return theRoll
    
    def getSize(self):
        return self.DieSize
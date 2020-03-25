import Analysis
import Entity
import EntityFactory
import SaveAndDelete

#List of accepted values to indicate user means yes
YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT", "TRUE"]

#Initial assumed yes
ContFlag = "Y"

#While the user wants to continue, keep running new scenarios
while ContFlag in YesValues:
    
    print("For the first fighter...")
    CharacterOne = SaveAndDelete.SaveAndDelete.LoadQuery()
    print("and for the second fighter...")
    CharacterTwo = SaveAndDelete.SaveAndDelete.LoadQuery()
    
    #appends one and two to the names so that the battle makes more sense if they are the same creature
    if CharacterOne.getName() == CharacterTwo.getName():
        CharacterOne.appendName(" One")
        CharacterTwo.appendName(" Two")
        
    #Create the Analysis object
    Battle = Analysis.Analysis(CharacterOne, CharacterTwo)
    
    #Give the probabilities and values to beat
    Battle.AnalyzeToHit()
    
    #Has the entities fight to the death
    #Prints out a play by play and declares the winner
    CharacterOne.CharactersFightToDeath(CharacterTwo)
    
    #Checks if the user would like to stop     
    ContFlag = str(input("Would you like to run the simulator again?")).upper()
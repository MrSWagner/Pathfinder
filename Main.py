import Analysis
import Entity
import EntityFactory

#List of accepted values to indicate user means yes
YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT"]

#Initial assumed yes
ContFlag = "Y"

#While the user wants to continue, keep running new scenarios
while ContFlag in YesValues:
    Make = EntityFactory.EntityFactory("Monsters.JSON")
    PC = EntityFactory.EntityFactory.buildNewPCFromUser()
    SC = Make.BuildEntityFromJSON()
    
    #Create the Analysis object
    Battle = Analysis.Analysis(PC, SC)
    
    #Give the probabilities and values to beat
    Battle.AnalyzeToHit()
    
    #Has the entities fight to the death
    #Prints out a play by play and declares the winner
    PC.CharactersFightToDeath(SC)
    
    #Checks if the user would like to stop     
    ContFlag = str(input("Would you like to run the simulator again?")).upper()
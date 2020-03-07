import Analysis
import Entity

#List of accepted values to indicate user means yes
YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT"]

#Initial assumed yes
ContFlag = "Y"

#While the user wants to continue, keep running new scenarios
while ContFlag in YesValues:
    PC = Entity.Entity.buildEntity()
    SC = Entity.Entity("Skeletal Champion", 2, 25, 19, 8, 8, 10, 5, 4)
    print("For this Beta Version, you will fight a set creature, a Skeletal Champion.")
    #Create the Analysis object
    Battle = Analysis.Analysis(PC, SC)
    
    #Give the probabilities and values to beat
    Battle.AnalyzeToHit()
      
    PC.CharactersFightToDeath(SC)
            
    ContFlag = str(input("Would you like to run the simulator again?")).upper()
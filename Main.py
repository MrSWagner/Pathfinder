import Analysis
import Entity

#List of accepted values to indicate user means yes
YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT"]

#Initial assumed yes
ContFlag = "Y"

#While the user wants to continue, keep running new scenarios
while ContFlag in YesValues:
    
    #Assume no errors each run
    ErrorFlag = False

    #Attempt to save each entered value as an integer
    
    try:
        print("Hello and welcome to the Pathfinder Second Edition Battle Simulator.")
        print("The following questions will establish one of the two fighters in the simulation:")
        Name = input("What is the character's name?")
        MaxHP = int(input("What is their Maximum number of Health Points?"))
        AC = int(input("What is their armor class?"))
        DieSize = int(input("What is the Damage Die Size on your main weapon (enter the number only)? "))
        Perception = int(input("What is their Perception Bonus?"))
        ToHitBonus = int(input("What is the Attack Bonus on your main weapon? "))
        MultAttackPenalty = int(input("What is their Multiple Attack Penalty (Default is 5)?"))
        DamageBonus = int(input("What is the Damage Bonus on your main weapon? "))
        
    #Any value other than integer will throw this exception
    #This also changes the ErrorFlag to indicate a restart is necessary
    except ValueError:
        print("Value Error: You may only enter integers.")
        ErrorFlag = True
    print("\n")

    #If there is an error, remind them of what they did wrong
    if ErrorFlag:
        print("Re-Enter Your Values Using Only Integers")
        print("\n")

    #In the case of no error, run the program
    else:
        PC = Entity.Entity(Name, MaxHP, AC, DieSize, Perception, ToHitBonus, MultAttackPenalty, DamageBonus)
        SC = Entity.Entity("Skeletal Champion", 25, 19, 8, 8, 10, 5, 4)
        print("For this Beta Version, you will fight a set creature, a Skeletal Champion.")
        #Create the Analysis object
        Battle = Analysis.Analysis(PC, SC)
        
        #Give the probabilities and values to beat
        Battle.AnalyzeToHit()
        
        PCInitiative = PC.Initiative()
        SCInitiative = SC.Initiative()
        
        if PCInitiative == SCInitiative:
            PCInitiative = PC.Initiative()
            SCInitiative = SC.Initiative()
            
            while PCInitiative == SCInitiative:
                PCInitiative = PC.Initiative()
                SCInitiative = SC.Initiative()
                
        if PCInitiative > SCInitiative:
            print("{} rolled a higher initiative!\n".format(PC.getName()))
            Dead = False
            RoundsCombat = 0
            while not Dead:
                RoundsCombat += 1
                Dead = PC.OneRound(SC)
                if Dead:
                    break
                Dead = SC.OneRound(PC)
                if Dead:
                    break
                
            PC.Loser(RoundsCombat)
            SC.Loser(RoundsCombat)
            
        else:
            print("{} rolled a higher initiative!".format(SC.getName()))
            Dead = False
            while not Dead:
                Dead = SC.OneRound(PC)
                if Dead:
                    break
                Dead = PC.OneRound(SC)
                if Dead:
                    break

            PC.Loser(RoundsCombat)
            SC.Loser(RoundsCombat)
            
    ContFlag = input("Would you like to run the simulator again?")
    ContFlag.upper()

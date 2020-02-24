import Match

#List of accepted values to indicate user means yes
YesValues = ["Y", "y", "yes", "Yes", "YES"]

#Initial assumed yes
ContFlag = "Y"

#By default the Multiple Attack Penalty is 5
MAP = 5

#While the user wants to continue, keep running new scenarios
while ContFlag in YesValues:
    
    #Assume no errors each run
    ErrorFlag = False

    #Attempt to save each entered value as an integer
    try:
        print("Hello and welcome to the PathfinderTwoHit application.")
        ToHitBonus = int(input("What is the attack bonus on your main weapon? "))
        DamageBonus = int(input("What is the damage bonus on your main weapon? "))
        DieSize = int(input("What is the damage die size on your main weapon (enter the number only)? "))
        AgileFlag = input("Is it an agile weapon? (Y or N)")
        EnemyAC = int(input("What is the AC of the enemy you are trying to hit? "))

    #Any value other than integer will throw this exception
    #This also changes the ErrorFlag to indicate a restart is nessisary
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
        #Create the Match object
        Battle = Match.Match(ToHitBonus, DamageBonus, DieSize, EnemyAC)
        
        #Give the probabilities and values to beat
        Battle.ToHitAnalysis()
        
        #If it's an Agile weapon, reduce the Multiple Attack Penalty to 4
        if AgileFlag in YesValues:
            MAP = 4
        
        #Simulate 10 rounds using the user input
        print("Here are 10 Example Rounds of Attacking with All 3 Actions:")
        print("\n")
        for i in range(1, 11):
            print("\n")
            print("Round {}:".format(i))
            print("\n")
            Battle.ExampleAttack(0*MAP)
            print("\n")
            Battle.ExampleAttack(1*MAP)
            print("\n")
            Battle.ExampleAttack(2*MAP)
        print("\n")

        #Ask for an update on their intent to continue
        ContFlag = input("Would you like to test another scenario (Y or N)?")


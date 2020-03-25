import json
import Entity

class EntityFactory:

    #Has the user enter data to build a new PC to use    
    def buildNewPCFromUser():
        ErrorFlag = False
        tryCount = 0
        while ErrorFlag or tryCount == 0:
            tryCount += 1
            try:
                print("Hello and welcome to the Pathfinder Second Edition Battle Simulator. ")
                print("The following questions will establish one of the two fighters in the simulation: ")
                Name = input("What is the character's name? ")
                Id = int(input("Give your character an ID number. "))
                Level = int(input("What is the character's level? "))
                Perception = int(input("What is their Perception Bonus? "))
                AC = int(input("What is their armor class? "))
                MaxHP = int(input("What is their Maximum number of Health Points? "))
                ToHitBonus = int(input("What is the Attack Bonus on your main weapon? "))
                MultAttackPenalty = int(input("What is their Multiple Attack Penalty (Default is 5)? "))
                DamageBonus = int(input("What is the Damage Bonus on your main weapon? "))
                DieSize = int(input("What is the Damage Die Size on your main weapon (enter the number only)? "))
        
            #Any value other than integer will throw this exception
            #This also changes the ErrorFlag to indicate a restart is necessary
            except ValueError:
                print("Value Error: You may only enter integers.")
                ErrorFlag = True
            print("\n")

            #If there is an error, remind them of what they did wrong
            if ErrorFlag:
                print("Re-Enter Number Values Using Only Integers")
                print("\n")
            
            else:
                
                return Entity.Entity(Id, Level, Name, Perception, AC, MaxHP, ToHitBonus, MultAttackPenalty, DamageBonus, DieSize)
    
    #Looks for the name in the Monsters.JSON file
    @staticmethod
    def MonsterLookup(EntityName):
        with open("Monsters.JSON", "r") as json_file:
            file = json.load(json_file)
            for entity in file:
                if EntityName in file:
                    return True
            return False
    
    #searches for a user saved file
    @staticmethod
    def SingleFileLookup(EntityName):
        EntityFileName = EntityName + ".json"
        #Opens and searches the file for the EntityID
        try:
            with open(EntityFileName, "r") as json_file:
                file = json.load(json_file)
                for entity in file:
                    if EntityName in file:
                        return True
        except:
            return False
    
    #Checks all locations for the entity
    #returns weather it is it's own file (FILE) or in the Monster.json file (MONSTER)
    #if it isn't in either location, returns 'NO'
    @staticmethod
    def CheckFiles(EntityName):
        #Checks for a user saved file
        lookupResult = EntityFactory.SingleFileLookup(EntityName)
        if lookupResult:
            return "FILE"
        #Checks for a monster
        lookupResult = EntityFactory.MonsterLookup(EntityName)
        if lookupResult:
            return "MONSTER"
        #Entity Not Found
        else:
            return "NO"
    
    #Builds an entity from the JSON file
    @staticmethod
    def BuildEntityFromJSON():
        #Ask user for an entity name and look for it
        EntityName = input(str("What is the name of the character? "))
        EntityName = EntityName.replace(' ', '')
        EntityName = EntityName.lower()
        lookupResult = EntityFactory.CheckFiles(EntityName)
        
        #if the entity isn't found, ask the user for a different monster
        while lookupResult == "NO":
            print("We couldn't find that character.")
            print("Check your spelling and try again.\n")
            EntityName = input(str("What is the name of the character? "))
            EntityName = EntityName.replace(' ', '')
            EntityName = EntityName.lower()
            lookupResult = EntityFactory.CheckFiles(EntityName)
            
        #create the filename
        if lookupResult == "MONSTER":
            FileName = "Monsters.JSON"
        else:
            FileName = EntityName + ".json"
            
        #Now that the entity is found and the filename is made, create the entity            
        with open(FileName, "r") as json_file:
            character = json.load(json_file)
            Id = character[EntityName]["Id"]
            Level = character[EntityName]["Level"]
            Name = character[EntityName]["Name"]
            Perception = character[EntityName]["Perception"]
            AC = character[EntityName]["AC"]
            HP = character[EntityName]["HP"]
            ToHitBonus = character[EntityName]["ToHitBonus"]
            MultAttackPenalty = character[EntityName]["multAttackPenalty"]
            DamageBonus = character[EntityName]["DamageBonus"]
            DieSize = character[EntityName]["DieSize"]
        return Entity.Entity(Id, Level, Name, Perception, AC, HP, ToHitBonus, MultAttackPenalty, DamageBonus, DieSize)

    

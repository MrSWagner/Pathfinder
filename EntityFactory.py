import json
import Entity

class EntityFactory:
    
    def __init__(self, fileName):
        self.fileName = str(fileName)

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
                Level = int(input("What is the character's level? "))
                MaxHP = int(input("What is their Maximum number of Health Points? "))
                AC = int(input("What is their armor class? "))
                DieSize = int(input("What is the Damage Die Size on your main weapon (enter the number only)? "))
                Perception = int(input("What is their Perception Bonus? "))
                ToHitBonus = int(input("What is the Attack Bonus on your main weapon? "))
                MultAttackPenalty = int(input("What is their Multiple Attack Penalty (Default is 5)? "))
                DamageBonus = int(input("What is the Damage Bonus on your main weapon? "))
        
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
                
                return Entity.Entity(Name, Level, MaxHP, AC, DieSize, Perception, ToHitBonus, MultAttackPenalty, DamageBonus)
            
    #searches through the file and returns true if the entity is present, false if it isn't
    def EntityLookup(self, EntityID):
        #Opens and searches the file for the EntityID
        with open(self.fileName, "r") as json_file:
            file = json.load(json_file)
            for entity in file:
                if EntityID in file:
                    return True
            return False
        
    #not complete       
    def BuildEntityFromJSON(self):
        #Ask user for monster name and look for it in the JSON file
        EntityID = input(str("What is the name of the monster? "))
        EntityID = EntityID.replace(' ', '')
        EntityID = EntityID.lower()
        lookupResult = self.EntityLookup(EntityID)
        
        #if the monster isn't found, ask the user for a different monster
        while not lookupResult:
            print("We couldn't find that monster.")
            print("Check your spelling and try again.\n")
            EntityID = input(str("What is the name of the monster? "))
            EntityID = EntityID.replace(' ', '')
            EntityID = EntityID.lower()
            lookupResult = self.EntityLookup(EntityID)
            
        #Now that the monster is found, create the entity            
        with open(self.fileName, "r") as json_file:
            monsters = json.load(json_file)
            HP = monsters[EntityID]["HP"]
            Level = monsters[EntityID]["level"]
            Name = monsters[EntityID]["name"]
            AC = monsters[EntityID]["AC"]
            DieSize = monsters[EntityID]["DieSize"]
            Perception = monsters[EntityID]["perception"]
            ToHitBonus = monsters[EntityID]["ToHitBonus"]
            MultAttackPenalty = monsters[EntityID]["multAttackPenalty"]
            DamageBonus = monsters[EntityID]["DamageBonus"]
        return Entity.Entity(Name, Level, HP, AC, DieSize, Perception, ToHitBonus, MultAttackPenalty, DamageBonus)

    

import json
import Entity
import os
import EntityFactory

class SaveAndDelete:
    #removes the spaces from a name and makes it all lowercase
    @staticmethod
    def PrepName(Entity):
        name = Entity.getName()
        name = name.replace(' ', '')
        name = name.lower()
        return name
    
    #creates a dictionary from an entity file
    @staticmethod    
    def CreateDictForJson(Entity, name):
        dictionary = {name:{
            "Id":Entity.getId(),
            "Level":Entity.getLevel(),
            "Name":Entity.getName(),
            "Perception": Entity.getPerception(),
            "AC": Entity.getAC(),
            "HP": Entity.getMaxHP(),
            "ToHitBonus": Entity.getToHitBonus(),
            "multAttackPenalty": Entity.getMultAttackPenalty(),
            "DamageBonus": Entity.getDamageBonus(),
            "DieSize": Entity.getDieSize()
            }
        }
        return dictionary
    
    #Saves the file and if it already exists, asks if the user would like to overwrite the file
    @staticmethod
    def SaveEntity(Entity):
        YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT", "TRUE"]
        #Converts the name into a standard style
        #sets the prepared name as the name of the dictionary
        #creates the dictionary for saving
        name = SaveAndDelete.PrepName(Entity)
        dictionary = SaveAndDelete.CreateDictForJson(Entity, name)
        #adds the .json to make it a filename
        #creates a file by that name and saves it
        FileName = name + ".json"
        try:
            with open(FileName, 'x') as Character_file:
                json.dump(dictionary, Character_file)
            print("Character saved as {}".format(FileName))
        except(FileExistsError):
            print("{} already exists.".format(FileName))
            overwrite = str(input("Do you want to overwrite {}?".format(FileName))).upper()
            if overwrite in YesValues:
                SaveAndDelete.DeleteEntity(FileName)
                with open(FileName, 'x') as Character_file:
                    json.dump(dictionary, Character_file)
                print("{} overwritten.".format(FileName))
    
    #deletes the character file        
    @staticmethod
    def DeleteEntity(fileName):
        if os.path.exists(fileName):
            os.remove(fileName)
        else:
            print("This file doesn't exist")
    
    #Asks the user if they would like to save, and saves if they say yes        
    @staticmethod
    def SaveQuery(Entity):
        YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT", "TRUE"]
        answer = str(input("Do you want to save {} for future battles? ".format(Entity.getName()))).upper()
        if answer in YesValues:
            SaveAndDelete.SaveEntity(Entity)
    
    @staticmethod
    def LoadQuery():
        YesValues = ["Y", "YEAH", "YUP", "AFFIRMATIVE", "YES", "CORRECT", "RIGHT", "TRUE"]
        answer = str(input("Do you want to load a saved character? ")).upper()
        if answer in YesValues:
            return EntityFactory.EntityFactory.BuildEntityFromJSON()

        elif answer not in YesValues:
            Character = EntityFactory.EntityFactory.buildNewPCFromUser()
            SaveAndDelete.SaveQuery(Character)
            return Character
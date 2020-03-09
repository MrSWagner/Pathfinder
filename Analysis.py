import Dice
import Entity

class Analysis:


    #Stores two entities as fighters A and B in the analysis object
    def __init__(self, Entity1, Entity2):
        self.fighterA = Entity1
        self.fighterB = Entity2
    
        
    #ToHitAnalysis runs several calculations and prints information to the user
    def AnalyzeToHit(self):
        
        #Both opponents use the same HitDie Size
        HitDieSize = self.fighterA.HitDice.getSize()
        
        #Pulls the name of each fighter
        fighterA_Name = self.fighterA.getName()
        fighterB_Name = self.fighterB.getName()
        
        #Pulls the AC of each fighter
        fighterA_AC= self.fighterA.getAC()
        fighterB_AC= self.fighterB.getAC()
        
        #Pulls the ToHitBonus for each fighter
        fighterA_THB= self.fighterA.getToHitBonus()
        fighterB_THB= self.fighterB.getToHitBonus()
        
        #Pulls the DamageBonus for each fighter
        fighterA_DB = self.fighterA.getDamageBonus()
        fighterB_DB = self.fighterB.getDamageBonus()
        
        #Pulls the DamageDie Size for each fighter
        fighterA_DDie = self.fighterA.DamageDice.getSize()
        fighterB_DDie = self.fighterB.DamageDice.getSize()
        
        
        #fighter A analysis to hit fighter B
        hit = 0
        crit = 0
        MinimumRollHit = 0
        CriticalRoll = 0
        for value in range(1, HitDieSize+1):
            if (((value + fighterA_THB) >= (fighterB_AC + 10)) and value == 1) or ((value + fighterA_THB) < fighterB_AC and value == 20 and (value + fighterA_THB + 10) >= fighterB_AC) or (((value + fighterA_THB) >= fighterB_AC) and value != 1):
                if hit == 0:
                    MinimumRollHit = value
                hit += 1
            if ((value + fighterA_THB) >= fighterB_AC + 10 and value != 1) or ((value + fighterA_THB) >= fighterB_AC and value == 20):
                if crit == 0:
                    CriticalRoll = value
                crit += 1
        
        MaxDamage = fighterA_DDie + fighterA_DB
        MinDamage = fighterA_DB + 1     #1 is the minimum roll on all dice
        PercentToHit = ((hit/HitDieSize)*100)//1
        PercentToCrit = ((crit/HitDieSize)*100)//1
        print("In a fight between {} and {}:\n".format(fighterA_Name, fighterB_Name))
        self.PrintResults(fighterA_Name, fighterB_Name, MaxDamage, MinDamage, MinimumRollHit, CriticalRoll, PercentToHit, PercentToCrit)

        
        #fighter B analysis to hit fighter A
        hit = 0
        crit = 0
        MinimumRollHit = 0
        CriticalRoll = 0
        for value in range(1, HitDieSize+1):
            if (value + fighterB_THB) >= fighterA_AC or (((value + fighterB_THB) >= fighterA_AC + 10) and value == 1) or ((value + fighterB_THB) < fighterA_AC and value == 20 and (value + fighterB_THB) >= fighterA_AC + 10):
                if hit == 0:
                    MinimumRollHit = value
                hit += 1
            if ((value + fighterB_THB) >= fighterA_AC + 10 and value != 1) or ((value + fighterB_THB) >= fighterA_AC and value == 20):
                if crit == 0:
                    CriticalRoll = value
                crit += 1
        
        MaxDamage = fighterB_DDie + fighterB_DB
        MinDamage = fighterB_DB + 1     #1 is the minimum roll on all dice
        PercentToHit = ((hit/HitDieSize)*100)//1
        PercentToCrit = ((crit/HitDieSize)*100)//1
        self.PrintResults(fighterB_Name, fighterA_Name, MaxDamage, MinDamage, MinimumRollHit, CriticalRoll, PercentToHit, PercentToCrit) 
        
    #Prints the results of the analysis
    def PrintResults(self, AttackerName, DefenderName, MaxDamage, MinDamage, MinimumRollHit, CriticalRoll, PercentToHit, PercentToCrit):
        avgHitDmg = (MaxDamage+MinDamage)//2
        print("{} has a {}% chance to hit {} (and a {}% chance to critically hit).".format(AttackerName, PercentToHit, DefenderName, PercentToCrit))
        
        if (CriticalRoll == 0 and MinimumRollHit == 0):
            print("{} cannot ever hit {}.".format(AttackerName, DefenderName))
            
        elif (CriticalRoll == MinimumRollHit):
            print("{} must roll a {} to critically hit, and cannot hit normally.".format(AttackerName, CriticalRoll))
            print("{} will critically hit for between {} and {} damage (average of {}).".format(AttackerName, 2*MinDamage, 2*MaxDamage, 2*avgHitDmg))
            
        elif CriticalRoll == 0:
            print("{} must roll a {} to hit, and cannot critically hit.".format(AttackerName, MinimumRollHit))
            print("{} will hit for between {} and {} damage (average of {})".format(AttackerName, MinDamage, MaxDamage, avgHitDmg))
            
        else:
            print("{} must roll a {} to hit, and a {} to critically hit.".format(AttackerName, MinimumRollHit, CriticalRoll))
            print("{} will hit for between {} and {} damage on a hit (average of {}) and between {} and {} damage on a critical hit (average of {})".format(AttackerName, MinDamage, MaxDamage, avgHitDmg, 2*MinDamage, 2*MaxDamage, 2*avgHitDmg))
        print("\n")

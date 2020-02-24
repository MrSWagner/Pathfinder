import Dice

class Match:


    #ToHitBonus is added to a roll of the HitDice
    #DamageBonus is added to damage, if the total ToHit is higher than the EnemyAC
    #DamageDieSize is the size of the die rolled for damage (added to DamageBonus)
    #EnemyAC is the total to beat or meet in order to roll damage
    #All ToHit calculations are done using the HitDice (size d20)
    def __init__(self, ToHitBonus, DamageBonus, DamageDieSize, EnemyAC):
        self.ToHitBonus = ToHitBonus
        self.DamageBonus = DamageBonus
        self.DamageDieSize = DamageDieSize
        self.EnemyAC = EnemyAC
        self.HitDice = Dice.Dice(20)
        self.DamageDice = Dice.Dice(DamageDieSize)

   
    #Damage calculates the total damage on a successful hit
    def Damage(self):
        return self.DamageDice.Roll() + self.DamageBonus
    
    #Prints the results of the analysis
    def PrintResults(self, MaxDamage, MinDamage, MinimumRollHit, CriticalRoll, PercentToHit, PercentToCrit, Nope):
        print("Below is an analysis of the match-up statistics: \n")
        print("Chance to Hit: {}%".format(PercentToHit))           
        print("Chance to Crit: {}%".format(PercentToCrit))
        if Nope == 0:
            print("You must roll a {} to hit".format(MinimumRollHit))
            print("You must roll a {} to critically hit".format(CriticalRoll))
            print("If you hit, you will do between {} and {} damage, with an average of {}".format(MinDamage, MaxDamage, (MinDamage+MaxDamage)//2))
            print("If you critically hit, you will do between {} and {} damage, with an average of {}".format(2*MinDamage, 2*MaxDamage, ((2*MinDamage)+(2*MaxDamage))//2))
        elif Nope == 1:
            print("You must roll a {} or more to hit".format(MinimumRollHit))
            print("If you hit, you will do between {} and {} damage".format(MinDamage, MaxDamage))
            print("Your average hit damage should be", (MinDamage+MaxDamage)//2)
        else:
            pass
            
    
    #ToHitAnalysis runs several calculations and prints information to the user
    def ToHitAnalysis(self):
        
        MaxDamage = self.DamageDieSize + self.DamageBonus
        MinDamage = self.DamageBonus + 1
        MinimumRollHit = self.EnemyAC - self.ToHitBonus
        CriticalRoll = MinimumRollHit + 10
        PercentToHit = ((20 - MinimumRollHit)/20)*100
        PercentToCrit = ((20 - CriticalRoll)/20)*100
        Nope = 0
        
        #SUPER low AC
        if CriticalRoll <= 1:
            CriticalRoll = 2
            MinimumRollHit = 1
            PercentToHit = 100
            PercentToCrit = 95
            
        #Low AC 
        elif MinimumRollHit <= 1:
            MinimumRollHit = 2
            PercentToHit = 95
            
        #High AC (Crit only on Nat 20)
        elif CriticalRoll >= 20 and  MinimumRollHit < 20 :
            PercentToCrit = 5
            CriticalRoll = 20
            
        #Edgecase: Crit or Miss
        elif MinimumRollHit == 20:
            PercentToCrit = 5
            PercentToHit = 5
            CriticalRoll = 20

        #SUPER High AC (No Hits, Nat 20 = Hit)
        #The Nope is a flag for the PrintResults Function
        elif MinimumRollHit > 20 and MinimumRollHit < 30:
            PercentToHit = 5
            PercentToCrit = 5
            MinimumRollHit = 20
            Nope = 1
            
        #Impossible AC (No Hits or Crits)
        #The Nope is a flag for the PrintResults Function
        elif MinimumRollHit >= 30:
            PercentToHit = 0
            PercentToCrit = 0
            Nope = 2
            
        self.PrintResults(MaxDamage, MinDamage, MinimumRollHit, CriticalRoll, PercentToHit, PercentToCrit, Nope)
        print("\n\n")



    #Role playing a single combat attack with randomized rolls
    #CritFlag indicates a natural 20(1) or natural 1(-1)
    #MAP is the multiple attack penatly modifier
    def ExampleAttack(self, MAP):
        EnemyAC = self.EnemyAC
        AttackRoll = self.HitDice.Roll()
        AttackTotal = AttackRoll + self.ToHitBonus - MAP
        CritFlag = 0
        if AttackRoll == 1:
            print("You rolled a Natural 1!")
            CritFlag = -1
        elif AttackRoll == 20:
            print("You rolled a Natural 20!")
            CritFlag = 1

        #Rolled a total higher than the enemy's AC (aka Normal Hit)
        if AttackTotal >= EnemyAC and AttackTotal < (EnemyAC+10) and CritFlag == 0:
            print("You hit with a {}!".format(AttackTotal))
            DamageRoll = self.Damage()
            print("You deal {} damage to the enemy!".format(DamageRoll))
            
        #Rolled a total higher than the enemy's AC + 10 (aka Normal Crit)
        elif AttackTotal >= (EnemyAC+10) and CritFlag != -1:
            print("You critically hit with a {}!".format(AttackTotal))
            DamageRoll = self.Damage() + self.Damage()
            print("You deal {} damage to the enemy!".format(DamageRoll))
            
        #Rolled a Natural 1 but still totaled 10 more than the enemy's AC (aka Nat 1 Crit)
        #Why are you even fighting this thing?
        elif AttackTotal >= (EnemyAC+10) and CritFlag == -1:
            print ("But you still hit with a {}".format(AttackTotal))
            DamageRoll = self.Damage()
            print("You deal {} damage to the enemy!".format(DamageRoll))

        #Rolled a Natural 20 and totalled above the enemies AC (aka a Nat 20 Crit)
        elif AttackTotal >= EnemyAC and AttackTotal < (EnemyAC+10) and CritFlag == 1:
            print("You critically hit with a {}!".format(AttackTotal))
            DamageRoll = self.Damage() + self.Damage()
            print("You deal {} damage to the enemy!".format(DamageRoll))
            
        #Rolled a Natural 20 but still totalled less than the enemies AC (aka Hail Mary Nat 20 Hit)
        elif AttackTotal < EnemyAC and AttackTotal > (EnemyAC-10) and CritFlag == 1:
            print("You would have missed with a {}, but still hit due to luck!".format(AttackTotal))
            DamageRoll = self.Damage()
            print("You deal {} damage to the enemy!".format(DamageRoll))

        #A Natural 1 killed the attack
        elif AttackTotal >= EnemyAC and AttackTotal < (EnemyAC+10) and CritFlag == -1:
            print("You missed with a {}.".format(AttackTotal))
            print("Better Luck Next Time")
            
        #Sucks to Suck, rolled too low
        else:
            print("You missed with a {}.".format(AttackTotal))
            print("Better Luck Next Time")
 

import Dice

class Entity:
    def __init__(self, Name, Level, MaxHP, AC, DieSize, Perception, ToHitBonus = 0, MultAttackPenalty = 5, DamageBonus = 0):
        self.Name = Name
        self.HP = MaxHP
        self.MaxHP = MaxHP
        self.AC = AC
        self.Level = Level
        self.DamageDice = Dice.Dice(DieSize)
        self.Perception = Perception
        self.ToHitBonus = ToHitBonus
        self.MultAttackPenalty = MultAttackPenalty
        self.DamageBonus = DamageBonus       
        self.HitDice = Dice.Dice()
        
    
    #returns the entity's Multiple Attack Penalty
    def getMultAttackPenalty(self):
        return self.MultAttackPenalty
    
    #returns the name of the entity
    def getName(self):
        return self.Name
    
    #returns the Max HP for an entity
    def getMaxHP(self):
        return self.MaxHP
    
    #returns current HP for an entity
    def getCurrentHP(self):
        return self.HP
     
    #returns the AC of the entity
    def getAC(self):
        return self.AC
    
    #returns the ToHitBonus of the entity
    def getToHitBonus(self):
        return self.ToHitBonus
    
    #returns the DamageBonus of the entity
    def getDamageBonus(self):
        return self.DamageBonus
    
    #Determines if the entity has been brought to 0 HP or not    
    def isDead(self):
        if self.getCurrentHP() <= 0:
            return True
        else:
            return False
        
    #returns the Perception of the entity
    def getPerception(self):
        return self.Perception
    
    #Reduces the entities HP by the amount of damage passed in
    def ApplyDamage(self, damage):
        self.HP = self.HP - damage

    #Returns a 0 for no hit, a 1 for a bit, and a 2 for a critical hit
    def didItHit(self, defender, actionInCombat):
        d20Roll = self.HitDice.Roll()
        print("{} rolled a {}".format(self.getName(), d20Roll))
        attackroll = d20Roll + self.ToHitBonus - (actionInCombat*self.getMultAttackPenalty())
        defenderAC = defender.getAC()
        hit = 0
        if (attackroll >= defenderAC) or ((attackroll >= defenderAC + 10) and d20Roll == 1) or ((attackroll < defenderAC) and (d20Roll == 20) and (attackroll >= defenderAC + 10)):
            hit += 1
        if ((attackroll >= defenderAC + 10) and (d20Roll != 1)) or ((attackroll >= defenderAC) and (d20Roll == 20)) and hit == 1:
            hit += 1
        return hit
        
    #Calculates the total damage on a successful hit
    def DamageRoll(self, multiplier = 1):
        return self.DamageDice.Roll(multiplier) + (self.DamageBonus * multiplier)
    
    #Rolls initiative and returns it
    def Initiative(self):
        return self.HitDice.Roll() + self.Perception
    
    #Identifies who lost after how many rounds
    def Loser(self, numRounds):
        if self.isDead():
                print("{} lost this battle after {} rounds.".format(self.getName(), numRounds))

    #Runs an action of combat for one combatant attacking a defender
    def BattleAction(self, defender, actionInCombat = 0):
        Attack = self.didItHit(defender, actionInCombat)
        
        #if the attack didn't hit
        if Attack == 0:
            print("{} Missed {}!\n".format(self.getName(), defender.getName()))
        
        #if the attack hit
        elif Attack == 1:
            dmg = self.DamageRoll()
            defender.ApplyDamage(dmg)
            print("{} hit {} for {} damage!".format(self.getName(), defender.getName(), dmg))
            print("{} has {} health left!\n".format(defender.getName(), defender.getCurrentHP()))
            
        #if the attack critically hit 
        elif Attack == 2:
            dmg = self.DamageRoll(2)
            defender.ApplyDamage(dmg)
            print("{} critically hit {} for {} damage!".format(self.getName(), defender.getName(), dmg))
            print("{} has {} health left!\n".format(defender.getName(), defender.getCurrentHP()))
 
    #Runs a single round of combat for an entity
    def OneRound(self, defender):
        actionInCombat = 0
        KnockOut = False
        while actionInCombat < 3 and not KnockOut:
            self.BattleAction(defender, actionInCombat)
            actionInCombat += 1
            if defender.isDead():
                KnockOut = True
                print("{} has been knocked out!".format(defender.getName()))
                return KnockOut
        return KnockOut


    def CharactersFightToDeath(self, SC):
        PCInitiative = self.Initiative()
        SCInitiative = SC.Initiative()
            
        while PCInitiative == SCInitiative:
            PCInitiative = self.Initiative()
            SCInitiative = SC.Initiative()
                
        if PCInitiative > SCInitiative:
            print("{} rolled a higher initiative!\n".format(self.getName()))
            Dead = False
            RoundsCombat = 0
            while not Dead:
                RoundsCombat += 1
                Dead = self.OneRound(SC)
                if Dead:
                    break
                Dead = SC.OneRound(self)
                if Dead:
                    break
                
            self.Loser(RoundsCombat)
            SC.Loser(RoundsCombat)
            
        else:
            print("{} rolled a higher initiative!".format(SC.getName()))
            Dead = False
            RoundsCombat = 0
            while not Dead:
                RoundsCombat += 1
                Dead = SC.OneRound(self)
                if Dead:
                    break
                Dead = self.OneRound(SC)
                if Dead:
                    break

            self.Loser(RoundsCombat)
            SC.Loser(RoundsCombat)
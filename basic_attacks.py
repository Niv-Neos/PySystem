import math as mt
import numpy as np
import random as rd
import engine as eg
import character_effects as ce

class Attack:

    def __init__(self):

        self.Name = Name

        ### Stats

        self.Harm = 0
        self.HarmType = ""
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = Sanity, 4 = Lust, 5 = Fear

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = (False, []) ### Apply to what
        self.MOIST = False

    def Effect(self, Attacker, Defender, Attack, Protection):
        Attacker = Attacker
        Defender = Defender
        Attack = Attack
        Protection = Protection
        Total = round(((Attack.Harm*(rd.uniform(Attack.Random[0],Attack.Random[1]))) - Protection.DR), 2)
        print("You hit the target! They are dealt", Total, Attack.HarmType, "damage.")
        Defender.Damage[Attack.Inflict] = Defender.Damage[Attack.Inflict] + Total
        

class Pheromone_Spray:

    def __init__(self):

        self.Name = "Pheromone Spray"

        ### Stats

        self.Harm = 10
        self.HarmType = "Lust"
        self.Inflict = 4 ### 0 = HP, 1 = FP, 2 = MP, 3 = Sanity, 4 = Lust, 5 = Fear
        self.Random = [0.80,1.20]
        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.MOIST = True

    def Effect(self, Attacker, Defender, Attack, Protection):
        Attacker = Attacker
        Defender = Defender
        Attack = Attack
        Protection = Protection
        Total = round(((Attack.Harm*(rd.uniform(Attack.Random[0],Attack.Random[1]))) - Protection.DR), 2)
        print("You hit the target! They are dealt", Total, Attack.HarmType, "damage.")
        Defender.Damage[Attack.Inflict] = Defender.Damage[Attack.Inflict] + Total
        ce.Lusting(Defender.Lust,-5,5)

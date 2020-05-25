import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

import character_effects as ce

class Attack:

    def __init__(self):

        Character = ce.Char()

        self.Name = ""

        ### Stats

        self.Harm = 0
        self.HarmType = ""
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [0.80,1.20]
        self.Knockback = 0

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.MOIST = False

    def Effect(self, Attacker, Defender, Attack, Protection, Additional_DR, External_Effect):
        Attacker = Attacker
        Defender = Defender
        Attack = Attack
        Protection = Protection
        Additional_DR = Additional_DR
        External_Effect = External_Effect
        Check = eg.DamageNameChecker(Attack.Inflict)
        Total = round(((Attack.Harm*(rd.uniform(Attack.Random[0],Attack.Random[1]))) - (Protection.DR + Additional_DR)), 2)
        Defender.Damage[Attack.Inflict] = Defender.Damage[Attack.Inflict] + Total
        print("You hit the target! They are dealt", Total, Attack.HarmType, "damage.")
        print("")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()

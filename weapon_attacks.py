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
import weapons as wp

class Attack:

    def __init__(self, weapon, user):

        Character = user
        Weapon = weapon ### Insert Weapon here
        Cal_i = eg.Minner((Character.Melee_Weapon[0]/100) + 0.65, 0.65, 1.25)
        Cal_ii = eg.Minner(Weapon.Weight, 1, Weapon.Weight)

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

class Slash:

    def __init__(self, weapon, user):

        Character = user
        Weapon = weapon ### Insert Weapon here
        Cal_i = eg.Minner((Character.Melee_Weapon[0]/100) + 0.60, 0.60, 1.30)
        Cal_ii = eg.Minner(Weapon.Weight, 1, Weapon.Weight)

        self.Name = "Slash"

        ### Stats

        self.Harm = (Character.ST/Cal_ii.result + (Character.DX/1.5)) * 1.5 * Weapon.Harm_Mod
        self.HarmType = ""
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.30]
        self.Knockback = Character.ST/40

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
        print("You can't parry with that limb until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Stab:

    def __init__(self, weapon, user):

        Character = user
        Weapon = weapon ### Insert Weapon here
        Cal_i = eg.Minner((Character.Melee_Weapon[0]/100) + 0.65, 0.65, 1.25)
        Cal_ii = eg.Minner(Weapon.Weight, 1, Weapon.Weight)

        self.Name = "Stab"

        ### Stats

        self.Harm = ((Character.ST/Cal_ii.result + (Character.DX/1.5))/2) * 2 * Weapon.Harm_Mod
        self.HarmType = ""
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [0.65,1.25]
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
        print("You can't parry with that limb until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()

class Hammer_Swing:

    def __init__(self, weapon, user):

        Character = user
        Weapon = weapon ### Insert Weapon here
        Cal_i = eg.Minner((Character.Melee_Weapon[0]/100) + 0.70, 0.70, 1.20)
        Cal_ii = eg.Minner(Weapon.Weight, 1, Weapon.Weight)

        self.Name = "Hammer Swing"

        ### Stats

        self.Harm = (((Character.ST/Cal_ii.result) + (Character.DX/1.5))/2) * Weapon.Harm_Mod
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [0.70,1.30]
        self.Knockback = mt.floor(1 * Weapon.Weight)

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
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

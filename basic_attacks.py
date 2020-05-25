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
import realm as world

class Attack:

    def __init__(self, user):

        Character = user

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

class Bite:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Bite"

        varible_damage = ph.Teeth_Change(Character)

        ### Stats

        self.Harm = Character.ST + (Character.DX/3) * 1.25
        self.HarmType = "Pierce"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
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
        print("You punched the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't parry with that limb until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()

class Strong_Punch:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Strong Punch"

        ### Stats

        self.Harm = Character.ST + (Character.DX/2)
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/10

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
        print("You punched the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't parry with that limb until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Strong_Claw:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Strong Claw"

        ### Stats

        self.Harm = (Character.ST/2) + (Character.DX/1.5) * 1.5
        self.HarmType = "Cut"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
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
        print("You slash the target with your claw. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't parry with that limb until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()

class Light_Punch:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.76, 0.76, 1.20)

        self.Name = "Light Punch"

        ### Stats

        self.Harm = Character.ST + (Character.DX/2) * 0.56
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/50

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
        print("You punched the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Light_Claw:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.76, 0.76, 1.20)

        self.Name = "Light Claw"

        ### Stats

        self.Harm = ((Character.ST/2) + (Character.DX/1.5) * 1.5) * 0.56
        self.HarmType = "Cut"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
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
        print("You slash the target with your claw. They are dealt", Total, Attack.HarmType, "damage.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()


class Heavy_Punch:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Strong Punch"

        ### Stats

        self.Harm = Character.ST + (Character.DX/2) + ((Character.ST)/mt.sqrt(2))
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST*10

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
        print("You punched the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Heavy_Claw:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Strong Claw"

        ### Stats

        self.Harm = ((Character.ST/2) + (Character.DX/1.5) * 1.5) + ((Character.ST)/mt.sqrt(3))
        self.HarmType = "Cut"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
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
        print("You slash the target with your claw. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        External_Effect.Attack_Effect()

class Side_Kick:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Side Kick"

        ### Stats

        self.Harm = Character.ST + (Character.DX/2)
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/25

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
        print("You kicked the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't make movement defenses until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Heavy_Kick:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Heavy Kick"

        ### Stats

        self.Harm = Character.ST + (Character.DX/2) + ((Character.ST)/mt.sqrt(2))
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/10

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
        print("You kicked the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Low_Kick:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.70, 0.70, 1.20)

        self.Name = "Low Kick"

        ### Stats

        self.Harm = (Character.ST*0.66) + (Character.DX/2)
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/60

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
        print("You kicked the target. They are dealt", Total, Attack.HarmType, "damage.")
        debuff = eg.Minner((6 - Character.DX/3), 0, 6)
        print("You get", debuff, "to your movement defenses until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()


class Pheromone_Spray:

    def __init__(self, user):

        self.Name = "Pheromone Spray"

        ### Stats

        self.Harm = 10
        self.HarmType = "Lust"
        self.Inflict = 5 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [0.80,1.20]
        self.Knockback = 0

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.MOIST = True

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
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        ce.Lusting(Defender.Damage[Attack.Inflict],-5,5)
        External_Effect.Attack_Effect()

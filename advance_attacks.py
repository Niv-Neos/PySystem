import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf
import realm as re

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

import character_effects as ce

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

class Slide_Kick:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.90, 0.90, 1.20) + (-0.30 + Character.Familiarities["Slide Kick"])

        self.Name = "Slide Kick"

        ### Stats

        self.Harm = (Character.ST/2) + (Character.DX/2)
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/20

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
        print("You slide down and kick the target. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        print("They fall down to the ground if able.")
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Over_Shoulder_Slam:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.90, 0.90, 1.20) + (-0.30 + Character.Familiarities["Over Shoulder Slam"])

        self.Name = "Over Shoulder Slam"

        ### Stats

        self.Harm = (Character.ST/10)
        self.HarmType = "Blunt"
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
        print("You grab their arm and slam them to the ground. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        print("They slam down to the ground if able. (Do a Collision effect if they slam to the ground)")
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Roll_Kicker:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.90, 0.90, 1.20) + (-0.30 + Character.Familiarities["Roll Kicker"])

        self.Name = "Roll Kicker"

        ### Stats

        self.Harm = (Character.ST/8)
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [Cal_i,1.20]
        self.Knockback = Character.ST/5

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
        print("You grab their arms and roll back, push kick them to the other side. They are dealt", Total, Attack.HarmType, "damage.")
        print("You can't defend until your next turn and you are on the ground laying back.")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        print("They are pushed away", Attack.Knockback, "meters. (Do a Collision effect if they slam to the ground)")
        ph.Knockback(Attack, Defender)
        External_Effect.Attack_Effect()

class Tunnel_Traveller:

    def __init__(self, user):

        Character = user
        Cal_i = eg.Minner((ce.Arm_Combat/100) + 0.90, 0.90, 1.20) + (-0.30 + Character.Familiarities["Tunnel Traveller"])

        self.Name = "Tunnel Traveller"

        ### Stats

        self.Harm = 0
        self.HarmType = "Blunt"
        self.Inflict = 0 ### 0 = HP, 1 = FP, 2 = MP, 3 = CP, 4 = Sanity, 5 = Lust, 6 = Fear
        self.Random = [0.99,1.01]
        self.Knockback = 0

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.MOIST = False

    def Effect(self, Attacker, Defender, Attack, Protection, Additional_DR, External_Effect, Floor):
        Attacker = Attacker
        Defender = Defender
        Attack = Attack
        Protection = Protection
        Additional_DR = Additional_DR
        External_Effect = External_Effect
        Check = eg.DamageNameChecker(Attack.Inflict)
        Total = round(((Attack.Harm*(rd.uniform(Attack.Random[0],Attack.Random[1]))) - (Protection.DR + Additional_DR)), 2)
        Defender.Damage[Attack.Inflict] = Defender.Damage[Attack.Inflict] + Total
        print("You grab the target, spin around and slam them to the ground. Dealing", Total, Attack.HarmType, "damage.")
        print("")
        print("They now have", Defender.Damage[Attack.Inflict], Check.Result)
        FA = ph.Floor_Area(Floor, Defender)
        ph.Collision(Defender, FA, Attacker.DX, 0)
        External_Effect.Attack_Effect()

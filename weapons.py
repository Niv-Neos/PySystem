import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Weapon:

    def __init__(self, hp = 0, dr = 0, height = 1, width = 1, length = 1, weight = 1, electricity = 0, rate_of_fire = 1, ammo = -1,
                    harm_mod = 1, name = "", discription = "", damage = [0], flammable = False, poisonous = [False, []],
                    raw_eatable = True, cook_eatable = True, moist = False, attacks_list = [""]):

        self.Name = ""
        self.Discription = ""

        ### Stats

        self.HP = 0
        self.DR = 0

        self.Damage = [0] ### 0 = HP

        self.Electricity = 0

        self.Height = 100 ### in centimeters
        self.Width = 100
        self.Length = 100
        self.Volume = self.Height * self.Width * self.Length

        self.Weight = 100 ### in kg

        self.Rate_Of_Fire = 1
        self.Ammo = -1 ### -1 means indefinity

        self.Harm_Mod = 1

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = False
        self.COOK_EATABLE = False
        self.MOIST = False

        self.ATTACKS_LIST = []

        def Attack_Effect(self):
            x = 0

Weapon_Test = Weapon(
hp = 0,
dr = 0,
height = 1,
width = 1,
length = 1,
weight = 1,
electricity = 0,
rate_of_fire = 1,
ammo = -1,
harm_mod = 1,
name = "",
discription = "",
damage = [0],
flammable = False,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False,
attacks_list = [""]
)

Long_Sword = Weapon(
hp = 17,
dr = 1,
height = 60,
width = 2.6,
length = 10,
weight = 1.1,
electricity = 0,
rate_of_fire = 1,
ammo = -1,
harm_mod = 1,
name = "Long Sword",
discription = "",
damage = [0],
flammable = False,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False,
attacks_list = ["Slash", "Stab"]
)

Nailing_Hammer = Weapon(
hp = 11,
dr = 1,
height = 28.4,
width = 2.5,
length = 10.5,
weight = 0.3,
electricity = 0,
rate_of_fire = 1,
ammo = -1,
harm_mod = 1,
name = "Nailing Hammer",
discription = "",
damage = [0],
flammable = False,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False,
attacks_list = ["Hammer Swing"]
)

Savior_Sword = Weapon(
hp = 18,
dr = 1,
height = 65,
width = 2.7,
length = 9,
weight = 1.1,
electricity = 0,
rate_of_fire = 1,
ammo = -1,
harm_mod = 1.17,
name = "Savior Sword",
discription = "Gifted by her father, Kakis, she wields this blade to slay the creatures of the realm, protecting the homes of the Savera town. It is made of tri-synth titanium alloy.",
damage = [0],
flammable = False,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False,
attacks_list = ["Slash", "Stab"]
)

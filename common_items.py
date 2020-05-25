import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Item:

    def __init__(self, hp = 0, dr = 0, height = 1, width = 1, length = 1, weight = 1, electricity = 0, name = "", discription = "",
                    damage = [0], flammable = False, poisonous = [False, []], raw_eatable = True, cook_eatable = True, moist = False):

        self.Name = name
        self.Discription = discription

        ### Stats

        self.HP = hp
        self.DR = dr

        self.Damage = damage ### 0 = HP

        self.Electricity = electricity

        self.Height = height ### in centimeters
        self.Width = width
        self.Length = length

        self.Weight = weight ### in kg
        self.Volume = self.Height * self.Width * self.Length

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = True
        self.COOK_EATABLE = True
        self.MOIST = False

Item_Test = Item(
hp = 0,
dr = 0,
height = 1,
width = 1,
length = 1,
weight = 1,
electricity = 0,
name = "",
discription = "",
damage = [0],
flammable = False,
poisonous = [False, []],
raw_eatable = False,
cook_eatable = False,
moist = False
)

### Cloths

Cape = Item(
hp = 3,
dr = 0,
height = 95,
width = 50,
length = 2.5,
weight = 0.8,
electricity = 0,
name = "Cape",
discription = "A back piece of cloth for the back.",
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = False,
cook_eatable = False,
moist = False
)

### Computers

Desktop_Computer = Item(
hp = 6,
dr = 0,
height = 48,
width = 48,
length = 23,
weight = 23,
electricity = 0,
name = "Desktop Computer",
discription = "",
damage = [0],
flammable = True,
poisonous = [True, ["Plastic"]],
raw_eatable = False,
cook_eatable = False,
moist = False
)

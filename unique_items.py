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

    def __init__(self):

        self.Name = Name
        self.Discription = ""

        ### Stats

        self.Tech_Level = 0

        self.HP = 0
        self.DR = 0

        self.Electricity = 0

        self.Height = 100 ### in centimeters
        self.Width = 100
        self.Length = 100

        self.Weight = 100 ### in kg

        ### Traits

        self.ELECTRICAL = False
        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = True
        self.COOK_EATABLE = True
        self.MOIST = False

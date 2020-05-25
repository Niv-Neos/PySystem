import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')


class Food:

    def __init__(self):

        self.Name = ""
        self.Discription = ""

        self.Vegetable = False
        self.Fruit = False
        self.Meat = False
        self.Grain = False

        ### Stats

        self.HP = 0

        self.Calories = 0
        self.Fat = 0
        self.Sodium = 0
        self.Sugar = 0
        self.Protein = 0

        self.Height = 100 ### in centimeters
        self.Width = 100
        self.Length = 100

        self.Weight = 1

        ### Traits

        self.FLAMMABLE = False
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = True
        self.COOK_EATABLE = True
        self.MOIST = False

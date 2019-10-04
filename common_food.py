import math as mt
import numpy as np

class Food:

    def __init__(self):

        self.Name = Name

        self.Vegetable = False
        self.Fruit = False
        self.Meat = False
        self.Dairy = False

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

class Poison_Fruit:

    def __init__(self):

        self.Name = "Poison Fruit"

        self.Vegetable = False
        self.Fruit = True
        self.Meat = False
        self.Dairy = False

        ### Stats

        self.HP = 0

        self.Calories = 0
        self.Fat = 0
        self.Sodium = 0
        self.Sugar = 0
        self.Protein = 0

        self.Height = 7 ### in centimeters
        self.Width = 8
        self.Length = 8

        self.Weight = 0.14


        ### Traits

        self.FLAMMABLE = False
        self.POISONOUS = [True, ["People A", "People B"]] ### Apply to what
        self.RAW_EATABLE = True
        self.COOK_EATABLE = True

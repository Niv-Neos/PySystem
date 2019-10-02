import math as mt
import numpy as np

class Item:

    def __init__(self):

        self.Name = Name

        ### Stats

        self.HP = 0
        self.DR = 0

        self.Electricity = 0

        ### Traits

        self.FLAMMABLE = False
        self.POISONOUS = (False, []) ### Apply to what
        self.RAW_EATABLE = True
        self.COOK_EATABLE = True
        self.MOIST = False

import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Species:

    def __init__(self):

        self.Name = ""
        self.Type = "Biological"

        self.SPEstat = 0
        self.ANAstat = 0
        self.CREstat = 0
        self.EMOstat = 0
        self.WILstat = 0

        self.STstat = 0
        self.DXstat = 0
        self.COstat = 0
        self.HTstat = 0
        self.PEstat = 0

        ### Base Secondary

        self.HPstat = 0
        self.FPstat = 0
        self.MPstat = 0

        self.Sanitystat = 0
        self.Luststat = 0
        self.Fearstat = 0

        self.Dodgestat = 0
        self.Movestat = 0

        self.DRstat = 0

        self.FLAMMABLE = True
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = False
        self.COOK_EATABLE = True
        self.MOIST = False

        '''
        '''

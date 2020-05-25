import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Kan:

    def __init__(self):

        self.Name = "Kan"
        self.Type = "Biological"

        self.SPEstat = 2
        self.ANAstat = 2
        self.CREstat = 2
        self.EMOstat = 2
        self.WILstat = 2

        self.STstat = 1
        self.DXstat = 2
        self.COstat = 0
        self.HTstat = -1
        self.PEstat = 1

        ### Base Secondary

        self.HPstat = 5
        self.FPstat = -5
        self.MPstat = 0

        self.Sanitystat = 10
        self.Luststat = -10
        self.Fearstat = 0

        self.Dodgestat = 0
        self.Movestat = 0

        self.DRstat = 0

        self.FLAMMABLE = True
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = False
        self.COOK_EATABLE = True
        self.MOIST = False

        self.SEXTYPE = "Tyromitive"

        '''
        Claw
        '''

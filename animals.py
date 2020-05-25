import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Name:

    def __init__(self):

        self.Name = ""
        self.Type = "Biological"
        self.Discription = ""

        self.SPEstat = -9
        self.ANAstat = -9
        self.CREstat = -9
        self.EMOstat = -9
        self.WILstat = -2

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

class Torn:

    def __init__(self):

        self.Name = "Torn"
        self.Type = "Biological"
        self.Discription = ""

        self.SPEstat = -9
        self.ANAstat = -9
        self.CREstat = -9
        self.EMOstat = -9
        self.WILstat = -6

        self.STstat = 1
        self.DXstat = -6
        self.COstat = 1
        self.HTstat = 1
        self.PEstat = -3

        ### Base Secondary

        self.HPstat = 10
        self.FPstat = -60
        self.MPstat = -80

        self.Sanitystat = -30
        self.Luststat = 15
        self.Fearstat = -50

        self.Dodgestat = -3
        self.Movestat = -2

        self.DRstat = 0

        self.FLAMMABLE = True
        self.POISONOUS = [False, []] ### Apply to what
        self.RAW_EATABLE = False
        self.COOK_EATABLE = True
        self.MOIST = False

        '''
        Horizon
        '''

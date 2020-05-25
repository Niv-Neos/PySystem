import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Trait:

    def __init__(self, type):

        self.Name = ""
        self.Type = type
        self.Description = ""
        self.Ruling = ""

        self.Changes = {"":0}

    def Effect(self):
        x = 0 

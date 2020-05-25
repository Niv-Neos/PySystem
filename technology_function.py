import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class BuildingTools:

    def __init__(self, tools = False, pullers = False, vehicles = False, additive = False,
    interlock = False, magnetism = False, cylax = False):
        num_i = 0
        if tools is True:
            num_i = num_i + 1
        if pullers is True:
            num_i = num_i + 1
        if vehicles is True:
            num_i = num_i + 1
        if additive is True:
            num_i = num_i + 1
        if interlock is True:
            num_i = num_i + 1
        if magnetism is True:
            num_i = num_i + 1
        if cylax is True:
            num_i = num_i + 1
        self.result = num_i

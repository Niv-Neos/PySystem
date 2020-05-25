import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import realm as re

class Main:

    def __init__(self, debug):

        self.DebugMode = debug ### 0 = off, 1 = on

Debug = Main(1)
Debug.__init__(1)

world_gravity = re.Realm()

import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Main:

    def __init__(self, debug):

        self.DebugMode = debug ### 0 = off, 1 = on

    def message(self):
        print("This is the calculator, this script is for searching items and making IDLE process.")
        print("Read the list below for more information.")
        print("")
        if self.DebugMode == 1:
            print("Debug Mode is on.")
        elif self.DebugMode == 0:
            print("Debug Mode is off.")
        else:
            print("Debug Mode is not valid. On Calculator.py, type 0 on main for no Debug and 1 for Debug mode on.")
            raise SystemExit
        ui = input(">: ")

test = Main(1)
play = Main(0)

test.message()

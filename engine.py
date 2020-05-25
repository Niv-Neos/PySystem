import math as mt
import numpy as np
import random as rd
import physics as ph
import species as sp
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Empty:
    def __init__(self):
        self.Name = "Empty"
    def Attack_Effect(self):
        x = 0

class Minner:

       def __init__(self, var, min, max):

              self.final = 0
              self.process = var
              if self.process >= max:
                     self.final = max - 0.1
              elif self.process <= min:
                     self.final = min + 0.1
              else:
                     self.final = var

              self.result = self.final

class Random_Direction:

    def __init__(self, starting = 0, ending = 360):
        step = 1
        if step == 1:
            if starting < 0 and ending > 360:
                starting = 0
                ending = 360
                step = 2
            elif starting < 0:
                starting = 0
                step = 2
            elif ending > 360:
                ending = 360
                step = 2
            else:
                step = 2

        if step == 2:
            if starting < ending:
                result = rd.randint(starting,ending)
                print(result, "degrees")
                if result >= 0 and result <= 20 or result >= 340 and result <= 360:
                    str_i = "north"
                    step = 3
                elif result > 20 and result < 40:
                    str_i = "north north east"
                    step = 3
                elif result >= 40 and result <= 50:
                    str_i = "north east"
                    step = 3
                elif result > 50 and result < 70:
                    str_i = "north east east"
                    step = 3
                elif result >= 70 and result <= 110:
                    str_i = "east"
                    step = 3
                elif result > 110 and result < 130:
                    str_i = "south east east"
                    step = 3
                elif result >= 130 and result <= 140:
                    str_i = "south east"
                    step = 3
                elif result > 140 and result < 160:
                    str_i = "south south east"
                    step = 3
                elif result >= 160 and result <= 200:
                    str_i = "south"
                    step = 3
                elif result > 200 and result < 220:
                    str_i = "south south west"
                    step = 3
                elif result >= 220 and result <= 230:
                    str_i = "south west"
                    step = 3
                elif result > 230 and result < 250:
                    str_i = "south west west"
                    step = 3
                elif result >= 250 and result <= 290:
                    str_i = "west"
                    step = 3
                elif result > 290 and result < 310:
                    str_i = "north west west"
                    step = 3
                elif result >= 310 and result <= 320:
                    str_i = "north west"
                    step = 3
                elif result > 320 and result < 340:
                    str_i = "north north west"
                    step = 3
                else:
                    str_i = "Unexpected Error"
                    step = 3
            else:
                print("Starting was not less then the Ending")

        self.Final_Direction = str_i

class DetermineGentials:

    def __init__(self, type, character):
        import character as char
        checked = char.character()
        if type is "Bone":
            if checked.Race.SEXTYPE is not "Dymitive" and not "Plafor" and checked.Gender is "Male":
                self.result = "Penis"
            elif checked.Race.SEXTYPE is "Dymitive" and checked.Gender is "Fale":
                self.result = "Venis"
            elif checked.Race.SEXTYPE is "Anthronic" and checked.Gender is "Fale":
                self.result = "Ovipositor"
        elif type is "Hole":
            if checked.Race.SEXTYPE is "Tyromitive" and checked.Gender is "Fale":
                self.result = "Vagina"
            elif checked.Race.SEXTYPE is "Dymitive" and checked.Gender is "Male":
                self.result = "Pagina"
        else:
            self.result = "Sprayer"

class DamageNameChecker:

    def __init__(self, check):
        self.list_i = ["HP Damage", "FP Depleted", "MP Depleted", "CP Down", "Sanity Loss", "Lust", "Fear"]
        self.Result = self.list_i[check]

class Cylax_Cost:

    def __init__(self, bit):
        if bit == bin(0):
            num_i = 0
        elif bit == bin(1):
            num_i = 1
        elif bit == bin(2):
            num_i = 1
        elif bit == bin(3):
            num_i = 2
        elif bit == bin(4):
            num_i = 1
        elif bit == bin(5):
            num_i = 2
        elif bit == bin(6):
            num_i = 2
        elif bit == bin(7):
            num_i = 3
        elif bit == bin(8):
            num_i = 1
        elif bit == bin(9):
            num_i = 2
        elif bit == bin(10):
            num_i = 2
        elif bit == bin(11):
            num_i = 3
        elif bit == bin(12):
            num_i = 2
        elif bit == bin(13):
            num_i = 3
        elif bit == bin(14):
            num_i = 3
        elif bit == bin(15):
            num_i = 4
        self.Result = num_i

class Cylax_Able:

    def __init__(self, charbit, bit):
        if bit == bin(0):
            num_i = 0
        elif bit == bin(1):
            num_i = 1
        elif bit == bin(2):
            num_i = 2
        elif bit == bin(3):
            num_i = 3
        elif bit == bin(4):
            num_i = 4
        elif bit == bin(5):
            num_i = 5
        elif bit == bin(6):
            num_i = 6
        elif bit == bin(7):
            num_i = 7
        elif bit == bin(8):
            num_i = 8
        elif bit == bin(9):
            num_i = 9
        elif bit == bin(10):
            num_i = 10
        elif bit == bin(11):
            num_i = 11
        elif bit == bin(12):
            num_i = 12
        elif bit == bin(13):
            num_i = 13
        elif bit == bin(14):
            num_i = 14
        elif bit == bin(15):
            num_i = 15
        self.Result = num_i
        self.Final = False
        self.Approval = charbit.Cylax_Value

    def Check(self):
        if self.Result == 0:
            self.Final = True
            return
        elif self.Result == 1:
            if (self.Approval == bin(0) or self.Approval == bin(2) or self.Approval == bin(4) or self.Approval == bin(6)
                or self.Approval == bin(8) or self.Approval == bin(10) or self.Approval == bin(12) or self.Approval == bin(14)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 2:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(4) or self.Approval == bin(5)
                or self.Approval == bin(8) or self.Approval == bin(9) or self.Approval == bin(12) or self.Approval == bin(13)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 3:
            if (self.Approval == bin(0) or self.Approval == bin(4) or self.Approval == bin(8) or self.Approval == bin(12)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 4:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(2) or self.Approval == bin(3) or self.Approval == bin(8)
                or self.Approval == bin(9) or self.Approval == bin(10)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 5:
            if (self.Approval == bin(0) or self.Approval == bin(2) or self.Approval == bin(8) or self.Approval == bin(10)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 6:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(8) or self.Approval == bin(9)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 7:
            if (self.Approval == bin(0) or self.Approval == bin(8)):
                self.Final = True
                return
            else:
                self.Final == False
                return
        elif self.Result == 8:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(2) or self.Approval == bin(3) or self.Approval == bin(4)
                or self.Approval == bin(5) or self.Approval == bin(6) or self.Approval == bin(7)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 9:
            if (self.Approval == bin(0) or self.Approval == bin(2) or self.Approval == bin(4) or self.Approval == bin(6) or self.Approval == bin(8) or
                self.Approval == bin(10) or self.Approval == bin(12) or self.Approval == bin(14)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 10:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(4) or self.Approval == bin(5)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 11:
            if (self.Approval == bin(0) or self.Approval == bin(4)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 12:
            if (self.Approval == bin(0) or self.Approval == bin(1) or self.Approval == bin(2) or self.Approval == bin(3)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 13:
            if (self.Approval == bin(0) or self.Approval == bin(2)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 14:
            if (self.Approval == bin(0) or self.Approval == bin(1)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        elif self.Result == 15:
            if (self.Approval == bin(0)):
                self.Final = True
                return
            else:
                self.Final = False
                return
        else:
            if cf.Debug.DebugMode == 1:
                print("Character's Cylax Value is not 0000 to 1111, ranging  from bin(0) to bin(15). Result will be False.")
                self.Final = False
            else:
                self.Final = False

def Cuberoot(num_i):
    return num_i ** (1. / 3)

def Call_Damage(character, damage):
    if damage is "HP":
        print("HP:", character.Damage[0])
    elif damage is "FP":
        print("FP:", character.Damage[1])
    elif damage is "MP":
        print("MP:", character.Damage[2])
    elif damage is "CP":
        print("CP:", character.Damage[3])
    elif damage is "Sanity":
        print("Sanity:", character.Damage[4])
    elif damage is "Lust":
        print("Lust:", character.Damage[5])
    elif damage is "Fear":
        print("Fear:", character.Damage[6])
    else:
        print("Error, one of the strings is either not a vaild character or damage type.")

def Check_Effects(character):
    print(character.Effects)

def Check_Conditions(character):
    print(character.POISONED)
    print(character.PREGNAUT)
    print(character.UNCONSCIOUS)
    print(character.BROKEN_ARMS)
    print(character.BROKEN_LEGS)
    print(character.DAZED)
    print(character.SHORTCURCUIT)
    print(character.BROKEN_WINGS)

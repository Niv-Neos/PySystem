import math as mt
import numpy as np
import random as rd
import species as sp

class Minner:

       def __init__(self,var,min,max):

              self.final = 0
              self.process = var
              if self.process >= max:
                     self.final = max - 0.1
              elif self.process <= min:
                     self.final = min + 0.1
              else:
                     self.final = var

              self.result = self.final

class random_direction:

    def __init__(self, starting = 0, ending = 360):
        step = 1
        if step == 1:
            if starting < 0 and ending > 360:
                starting = 0
                ending = 360
                step = 2
                return
            elif starting < 0:
                starting = 0
                step = 2
                return
            elif ending > 360:
                ending = 360
                step = 2
                return
            else:
                step = 2

        if step == 2:
            if starting < ending:
                result = rd.randint(starting,ending)
                print(result, "degrees")
                if result >= 0 and result <= 20 or result >= 340 and result <= 360:
                    print("north")
                    step = 3
                    return
                elif result > 20 and result < 40:
                    print("north north east")
                    step = 3
                    return
                elif result >= 40 and result <= 50:
                    print("north east")
                    step = 3
                elif result > 50 and result < 70:
                    print("north east east")
                    step = 3
                    return
                elif result >= 70 and result <= 110:
                    print("east")
                    step = 3
                    return
                elif result > 110 and result < 130:
                    print("south east east")
                    step = 3
                    return
                elif result >= 130 and result <= 140:
                    print("south east")
                    step = 3
                    return
                elif result > 140 and result < 160:
                    print ("south south east")
                    step = 3
                    return
                elif result >= 160 and result <= 200:
                    print("south")
                    step = 3
                    return
                elif result > 200 and result < 220:
                    print("south south west")
                    step = 3
                    return
                elif result >= 220 and result <= 230:
                    print("south west")
                    step = 3
                    return
                elif result > 230 and result < 250:
                    print("south west west")
                    step = 3
                    return
                elif result >= 250 and result <= 290:
                    print("west")
                    step = 3
                    return
                elif result > 290 and result < 310:
                    print("north west west")
                    step = 3
                    return
                elif result >= 310 and result <= 320:
                    print("north west")
                    step = 3
                    return
                elif result > 320 and result < 340:
                    print("north north west")
                    step = 3
                    return
                else:
                    print("Unexpected Error")
                    step = 3
                    return
            else:
                print("Starting was not less then the Ending")
                return
        while step == 3:
            break

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

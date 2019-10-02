import math as mt
import numpy as np
import random as rd
import engine as eg
import species as sp

'''
This file is for handling effects that influence characters themselves.
'''

import character_sheet as char
import common_species as species

Character = char.Char()

def Lusting(Lust,randvar_i,randvar_ii):
    ### Lust is based on Character.Damage[4]
    step = 1
    if randvar_i > randvar_ii:
        print("Error: randvar_i can't be greater than randvar_ii.")
        step = 2
    else:
        step = 2
    if step == 2:
        result = rd.uniform(randvar_i,randvar_ii,) + Lust
        if result > 0*(Character.Lust/100) and result <= 10*(Character.Lust/100):
            print("You feel something but it's nothing.")
            step = 3
            return
        elif result > 10*(Character.Lust/100) and result <= 19*(Character.Lust/100):
            print("You are a little tingled. It may be a small distraction.")
            step = 3
            return
        elif result > 19*(Character.Lust/100) and result <= 39*(Character.Lust/100):
            print("You are feeling ecstatic. It would be nice to have some fun.")
            step = 3
            return
        elif result > 39*(Character.Lust/100) and result <= 59*(Character.Lust/100):
            roll_i = rd.randint(1,4)
            step = 3
            return
            if roll_i >= 1 and result < 4:
                print("You are feeling lustful, finding it hard to concentrate.")
                step = 3
                return
            elif roll_i == 4:
                print("You stand in lust, may be staring on something, enticing.")
                print("You ogle for", (Lust/(Character.WIL*5)), "seconds.")
                step = 3
                return
        elif result > 59*(Character.Lust/100) and result <= 79*(Character.Lust/100):
            roll_ii = rd.randint(1,5)
            if roll_ii >= 1 and result < 3:
                print("You are feeling lustful, finding it hard to concentrate.")
                step = 3
                return
            elif roll_ii >= 3 and result < 5:
                print("You stand in lust, may be staring on something, enticing.")
                print("You ogle for", (Lust/(Character.WIL*5)), "seconds.")
                step = 3
                return
            elif roll_ii == 5:
                misstep = ["fall down laying", "hit the nearest, adjacent object. (If none then fall down)", "touch the distraction",
                            "touch your genitals", "ask if you want to go out. (If not a person, you mate it or masturbate to it)"]
                print("You are so distracted that you", misstep[rd.randint(0,4)])
                step = 3
                return
        elif result > 79*(Character.Lust/100) and result <= 99*(Character.Lust/100):
            roll_iii = rd.randint(1,7)
            if roll_iii == 1:
                print("You are feeling lustful, finding it hard to concentrate.")
                step = 3
                return
            elif roll_iii > 1 and result <= 3:
                print("You stand in lust, may be staring on something, enticing.")
                print("You ogle for", (Lust/(Character.WIL*5)), "seconds.")
                step = 3
                return
            elif roll_iii > 3 and result <= 6:
                misstep = ["fall down laying", "hit the nearest, adjacent object. (If none then fall down)", "touch the distraction",
                            "touch your genitals", "ask if you want to go out. (If not a person, you mate it or masturbate to it)"]
                print("You are so distracted that you", misstep[rd.randint(0,4)])
                step = 3
                return
            elif roll_iii == 7:
                misstep_ii = ["try to mate something.", "force yourself on someone.", "take off your wear and masturbate."]
                print("You can't take it any more, you", misstep_ii[rd.randint(0,2)])
                step = 3
                return
            elif result >= 100*(Character.Lust/100):
                misstep_ii = ["try to mate something.", "force yourself on someone.", "take off your wear and masturbate."]
                print("You have completely lost it, so absorbed in your lust, you", misstep_ii[rd.randint(0,2)])
                step = 3
                return
    if step == 3:
        if ((char.Race.SEXTYPE is "Tyromitive" and char.Gender is "Male") or (char.Race.SEXTYPE is "Dymitive" and char.Gender is
            "Fale")) and result >= 50:
            check = eg.DetermineGentials("Bone")
            print("Your", check.result, "hardens up and sticks out.")
            step = 4
        elif ((char.Race.SEXTYPE is "Tyromitive" and char.Gender is "Fale") or (char.Race.SEXTYPE is "Dymitive" and char.Gender is
            "Male")) and result >= 50:
            check = eg.DetermineGentials("Hole")
            print("Your", check.result, "is moist and wet.")
            step = 4
        elif result < 50:
            step = 4
        else:
            print("You are struggling to keep a decent posture.")
            step = 4
    while step == 4:
        break

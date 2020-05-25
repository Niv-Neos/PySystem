import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

'''
This file is for handling effects that influence characters themselves.
'''

import character_sheet as char
import common_species as species
import realm as world

Character = char.Char()

def Confusion(Sanity):
        result = rd.uniform(1,Sanity) + Sanity
        if result >= 75:
            print("You're are losing a grip with yourself. (The GM decides your next action)")
        else:
            print("You are fine.")


def Lusting(Lust, randvar_i, randvar_ii):
    ### Lust is based on Character.Damage[5]
    step = 1
    if randvar_i > randvar_ii:
        print("Error: randvar_i can't be greater than randvar_ii.")
    elif Character.Lust is "None":
        print("You cannot experience sexual pleasures.")
    else:
        step = 2
    if step == 2:
        result = rd.uniform(randvar_i,randvar_ii) + Lust
        if result > 0*(Character.Lust/100) and result <= 10*(Character.Lust/100):
            print("You feel something, but it's nothing.")
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
            else:
                print("You feel nothing.")
                step = 3
                return
    if step == 3:
        if ((char.Species.SEXTYPE is "Tyromitive" and char.Gender is "Male") or (char.Species.SEXTYPE is "Dymitive" and char.Gender is
            "Fale")) and result >= 50:
            check = eg.DetermineGentials("Bone")
            print("Your", check.result, "hardens up and sticks out.")
            step = 4
        elif ((char.Species.SEXTYPE is "Tyromitive" and char.Gender is "Fale") or (char.Species.SEXTYPE is "Dymitive" and char.Gender is
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

def Fright(Fear, randvar_i, randvar_ii):
    step = 1
    if randvar_i > randvar_ii:
        print("Error: randvar_i can't be greater than randvar_ii.")
    elif Character.Fear is "None":
        print("You are fearless")
    else:
        step = 2
    if step == 2:
        result = rd.uniform(randvar_imrandvar_ii) + Fear
        if result > 0*(Character.Fear/100) and result <= 10*(Character.Fear/100):
            print("You are wary, but it's whatever.")
            step = 3
            return
        elif result > 10*(Character.Fear/100) and result <= 19*(Character.Fear/100):
            print("You are timid, being concerned.")
            step = 3
            return
        elif result > 19*(Character.Fear/100) and result <= 39*(Character.Lust/100):
            print("You are scared, acting up.")
            step = 3
            return
        elif result > 39*(Character.Fear/100) and result <= 59*(Character.Lust/100):
            roll_i = rd.randint(1,4)
            step = 3
            return
            if roll_i >= 1 and result < 4:
                print("You are fearful, being very cautious.")
                step = 3
                return
            elif roll_i == 4:
                print("You are shaken.")
                print("You shiffer in place for", (Fear/(Character.WIL*5)), "seconds.")
                step = 3
                return
        elif result > 59*(Character.Fear/100) and result <= 79*(Character.Fear/100):
            roll_ii = rd.randint(1,5)
            if roll_ii >= 1 and result < 3:
                print("You are fearful, being very cautious")
                step = 3
                return
            elif roll_ii >= 3 and result < 5:
                print("You are shaken.")
                print("You shiffer in place for", (Lust/(Character.WIL*5)), "seconds.")
                step = 3
                return
            elif roll_ii == 5:
                misstep = ["run away from the threat (You think there's a threat)", "stay frozen in place until something moves. (or after about a minute)", "attack in fright (No accuracies)",
                            "yell at the threat in a way to get it away from you", "cry for help", "find a way to end the threat irrationally (The GM decides)"]
                print("Scared, you", misstep[rd.randint(0,5)])
                step = 3
                return
        elif result > 79*(Character.Fear/100) and result <= 99*(Character.Fear/100):
            roll_iii = rd.randint(1,7)
            if roll_iii == 1:
                print("You are fearful, being very cautious")
                step = 3
                return
            elif roll_iii > 1 and result <= 3:
                print("You are shaken.")
                print("You shiffer in place for", (Lust/(Character.WIL*5)), "seconds.")
                step = 3
                return
            elif roll_iii > 3 and result <= 6:
                misstep = ["run away from the threat (You think there's a threat)", "stay frozen in place until something moves. (or after about a minute)", "attack in fright (No accuracies)",
                            "yell at the threat in a way to get it away from you", "cry for help", "find a way to end the threat irrationally (The GM decides)"]
                print("Scared, you", misstep[rd.randint(0,5)])
                step = 3
                return
            elif roll_iii == 7 and Character.Lust < 51 and Character.Sanity < 51:
                misstep_ii = ["run away aimlessly (GM decides).", "attack irrationally (GM decides).", "scream in panic.", "faint."]
                print("Of seer fright, you", misstep_ii[rd.randint(0,3)])
                step = 3
                return
            elif roll_iii == 7 and Character.Lust >= 51 and Character.Sanity < 51:
                misstep_ii = ["run away aimlessly (GM decides).", "attack irrationally (GM decides).", "scream in panic.", "faint.", "masturbate furiously.", "desperately beg for sex."]
                print("Of seer fright, you", misstep_ii[rd.randint(0,5)])
                step = 3
                return
            elif roll_iii == 7 and Character.Lust < 51 and Character.Sanity >= 51:
                misstep_ii = ["run away aimlessly (GM decides).", "attack irrationally (GM decides).", "scream in panic.", "faint.", "lose your mind (GM decides)", "do something completely random (GM decides)"]
                print("Of seer fright, you", misstep_ii[rd.randint(0,5)])
                step = 3
                return
        elif result >= 100*(Character.Fear/100):
            if Character.Lust < 51 and Character.Sanity < 51:
                misstep_ii = ["Panicly run away aimlessly (GM decides).", "attack irrationally with half skill rating (GM decides).", "faint."]
                print("Fulfilled with fear, you", misstep_ii[rd.randint(0,2)])
                step = 3
                return
            elif Character.Lust >= 51 and Character.Sanity < 51:
                misstep_ii = ["Panicly run away aimlessly (GM decides).", "attack irrationally with half skill rating (GM decides).", "faint.", "masturbate desperately and furiously", "submit yourself."]
                print("Fulfilled with fear, you", misstep_ii[rd.randint(0,4)])
                step = 3
                return
            elif Character.Lust < 51 and Character.Sanity >= 51:
                misstep_ii = ["Panicly run away aimlessly (GM decides).", "attack irrationally with half skill rating (GM decides).", "faint.", "lose your mind, developing a weakness (GM decides)", "do something completely random (GM dcides)"]
                print("Fulfilled with fear, you", misstep_ii[rd.randint(0,4)])
                step = 3
                return
        else:
            print("You feel nothing.")
            step = 3
            return
    while step == 3:
        break

def Cylax_Overcharge(character):
    Overcharge = character.Damage[3] - character.CP
    character.Damage[3] = round(character.CP - rd.uniform(0.00,(10/character.CP)), 2)
    character.Damage[0] = round(character.Damage[0] + Overcharge, 2)
    print("You are overcharged of Cylax, releasing from your body, you suffer", Overcharge, "damage.")
    if Overcharge > (character.CO*10)/20:
        print("You are stunned for", Overcharge/5, "seconds.")
    if Overcharge > (character.CO*10)/10:
        print("You suffer from Cylax sickness, you can't use Cylax manipulation for", Overcharge, "seconds.")
    if Overcharge > (character.CO*10)/2:
        print("You fall unconscious.")
    if Overcharge > (character.CO*10):
        print("Your body is fatalized.")
        step_i = rd.randint(1,3)
        step_ii = 0
        while step_ii < step_i:
            num_i = rd.randint(1,100)
            if num_i >= 1 and num_i < 11:
                print("Your torso is torn apart.")
                step_ii = step_ii + 1
            elif num_i >= 11 and num_i < 18:
                arm_i = rd.randint(1,2)
                if arm_i == 1:
                    print("Your left arm is blasted.")
                    step_ii = step_ii + 1
                elif arm_i == 2:
                    print("Your right arm is blasted.")
                    step_ii = step_ii + 1
            elif num_i >= 18 and num_i < 20:
                eye_i = rd.randint(1,2)
                if eye_i == 1:
                    print("Your left eye is blasted.")
                    step_ii = step_ii + 1
                elif eye_i == 2:
                    print("Your right eye is blasted.")
                    step_ii = step_ii + 1
            elif num_i >= 20 and num_i < 26:
                print("Your face is blasted apart.")
            elif num_i >= 26 and num_i < 32:
                foot_i = rd.randint(1,2)
                if foot_i == 1:
                    print("Your left foot is blasted.")
                    step_ii = step_ii + 1
                elif foot_i == 2:
                    print("Your right foot is blasted.")
                    step_ii = step_ii + 1
            elif num_i >= 32 and num_i < 40:
                print("Your genitals tear off.")
            elif num_i >= 40 and num_i < 45:
                hand_i = rd.randint(1,2)
                if hand_i == 1:
                    print("Your left hand is blasted.")
                    step_ii = step_ii + 1
                elif hand_i == 2:
                    print("Your right hand is blasted.")
                    step_ii = step_ii + 1
            elif num_i >= 45 and num_i < 53:
                leg_i = rd.randint(1,2)
                if leg_i == 1:
                    print("Your left leg is blasted.")
                    step_ii = step_ii + 1
                elif leg_i == 2:
                    print("Your right leg is blasted.")
                    step_ii = step_ii + 1
            elif num_i >= 53 and num_i < 61:
                print("A limb tears off.")
            elif num_i >= 61 and num_i < 67:
                print("A neck explods.")
            elif num_i >= 67 and num_i < 71:
                print("Your Skull blows up.")
            elif num_i >= 71 and num_i < 83:
                print("Your tail blows off.")
            else:
                print("You bleed out, becoming dazed.")

def Sex(character_i, character_ii = 0, type = "Fale to Male", skill = 0, same_species = True, objects = [""]):
    ### Types: Fale to Male, Fale to Fale, Male to Male, Fetish, Masturbation
    if character_ii == 0 and type != "Masturbation":
        print("You can't have sex with nothing.")
    elif type == "Fale to Male":
        num_i = 1
        if "Condom" in objects:
            condom_on = True
            return
        else:
            condom_on = False
            return
    elif type == "Fale to Fale" or type == "Male to Male":
        num_i = 0.8
        return
    elif type == "Fetish":
        if (type in character_i.Traits and type not in character_ii.Traits) or (type not in character_i.Traits and
            type in character_ii.Traits):
            num_i = 0.6
            return
        elif type not in character_i.Traits and type not in character_ii.Traits:
            num_i = 0.01
            return
        elif type in character_i.Traits and type in character_ii.Traits:
            num_i = 0.7
            return
        else:
            num_i = 0
            return
    elif type == "Masturbation":
        num_i = 0.5
        return
    time = (100 + character_i.Lust + character_ii.Lust) - (character_i.Damage[5] + character_i.Damage[5]) / ((character_i.HT/20) + (character_ii.HT/20)) * num_i
    character_i.Damage[1] = round(character_i.Damage[1] + time/20, 2)
    character_ii.Damage[2] = round(character_ii.Damage[1] + time/50, 2)
    character_i.Damage[5] = 0
    character_ii.Damage[5] = 0
    print(character_i.Name, "and", character_ii.Name, "have sex for", time, "seconds.", "(", time/60, "minutes. )")
    print("After sex,", character_i.Name, "now have", round(character_i.Damage[1]*num_i), "HP and", character_i.Damage[2], "MP depleted.")
    print("After sex,", character_ii.Name, "now have", round(character_ii.Damage[1]*num_i), "HP and", character_ii.Damage[2], "MP depleted.")
    print(character_i.Name, "and", character_ii.Name, "have lost all their lost, reduced to 0.")

    if type == "Fale to Male":
        ph.Impregnation_Check(character_i, character_ii, "Sex", condom_on)

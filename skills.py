import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

import character_sheet as char
import character_sheet as defender
import advance_attacks as aa
import basic_attacks as ba
import weapon_attacks as wa
import character_sheet as protect
import weapons as wp
import common_items as item
import common_food as food

def Generic_Skill(character = char.Char(), personal = 0, familiarity = 0, technology = 0, extra_against = 0, extra_for = 0, accuracy = 0,
    difficulty = 0, skill = "Cylaxian"):


    Skill_User = character

    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Rating = list_i[dict_i[skill]]

    Personal = personal
    Familiarity = familiarity
    Technology = technology
    Extra_Against = extra_against
    Extra_For = extra_for
    Accuracy = accuracy

    Difficulty = difficulty

    Cal_i = eg.Minner((Accuracy/20) + 0.80, 0.80, 1.20)

    S = round((Rating + Personal + Accuracy) * round(rd.uniform(0.80, 1.20), 2) -
    (Difficulty * ((1 + Extra_Against) / (1 + Familiarity + Technology + Extra_For))), 2)

    print(S)

    if S > 0:
        print(Skill_User.Name, "succeed the challenge.")

    elif S <= 0:
        print(Skill_User.Name, "failed the challenge.")

    else:
        print("Something have went wrong. Most likely due to S not being a float.")

def Attacking(char_att = char.Char(), char_def = char.Char(), external_effect = eg.Empty(),
    attack = ba.Attack(None), protect = char.Char(), additional_dr = 0, familiarity = 0, technology = 0, personal = 0, accuracy = 0,
    extra_against = 0, extra_for = 0, cover = 0, vision = 0, range = 0, hit_zone = 0, inability = 0, preperation = 0,
    skill_att = "Arm_Combat", difficulty = "Arm_Combat"):


    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}
    dict_ii = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]
    list_ii = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Attacker = char_att
    Defender = char_def
    Attack = attack ### Weapons need to be called
    Protection = protect

    Additional_DR = additional_dr

    External_Effect = eg.Empty()

    Familiarity = familiarity
    Technology = technology

    Rating = list_i[dict_i[skill_att]]
    Personal = personal
    Accuracy = accuracy
    Extra_Against = extra_against
    Extra_For = extra_for
    Cover = cover
    Vision = vision
    Range = range

    Hit_Zone = hit_zone
    Inability = inability
    Difficulty = abs(5 + list_ii[dict_ii[skill_def]] + Hit_Zone - Inability)
    Preperation = preperation

    '''
    Hit Zones

    Arm (2)
    Eye (9)
    Face (5)
    Foot (4)
    Groin (3)
    Hand (4)
    Leg (2)
    Limb (2)
    Neck (5)
    Skull (7)
    Tail (2)
    Torso (0)

    Add bonuses and penalities if they are abnormally larger or shorter than the body.
    '''

    Damage = ((Attacker.Damage[0]/((Attacker.Height/33) + (Attacker.Width/33) + (Attacker.Length/33) + ((Attacker.CO)*10)))) + ((Attacker.Damage[1]/10) * (Attacker.Weight/100)
     / ((Attacker.HT)*10)) + (Attacker.Damage[2]/(Attacker.WIL*10)) + (Attacker.Damage[3]/(Attacker.WIL*10)) + (Attacker.Damage[4]/(Attacker.WIL*10)) + (Attacker.Damage[5]/
     (Attacker.WIL*10)) ### Damage on the attacker(m)

    Cal_i = eg.Minner((Accuracy/20) + 0.80, 0.80, 1.20)
    Cal_ii = eg.Minner((Preperation/20) + 0.80, 0.80, 1.20)

    S = round((((Rating + Personal + Accuracy) * round(rd.uniform(Cal_i.result, 1.20), 2) -
    (Difficulty * ((1 + Cover + Damage + Vision + Range + Extra_Against ) / (1 + Familiarity + Technology + Extra_For))
    * round(rd.uniform(Cal_ii.result, 1.20), 2)))), 2)

    print(S)

    if S > 0:
        Attack.Effect(Attacker, Defender, Attack, Protection, Additional_DR, External_Effect)

    else:
        print("You miss the target.")

def Cooking(character = char.Char(), food_item = food.Food(), personal = 0, familiarity = 0, technology = 0, extra_against = 0,
    extra_for = 0, difficulty = 0, skill = "Cooking"):

    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Cooker = character
    Food_Item = food_item

    Rating = list_i[dict_i[skill]] ### (r)
    Personal = personal ### Enter Personality and Emotional Factors (p)
    Familiarity = familiarity
    Technology = technology
    Extra_Against = extra_against ### Any Additional Factors (e_n)
    Extra_For = extra_for ### Any Additional Factors (e_d)

    Difficulty = difficulty ### (d)

    S = round((((Rating + Personal) * rd.uniform(0.80,1.20), 2)) - (Difficulty * ((1 + Extra_Against) / (1 + Familiarity +
    Technology + Extra_For))), 2)

    print(S)

    if S > 0 and S <= 5:
        print(Cooker.Name, "successifully cooked the", Food_Item.Name, ". It's decent quality.")

    if S > 5 and S <= 12:
        print(Cooker.Name, "successifully cooked a delicious meal of", Food_Item.Name, ". It's good quality.")

    if S > 12 and S <= 18:
        print(Cooker.Name, "successifully cooked an amazing meal of", Food_Item.Name, ". It's great quality")

    if S > 18:
        print(Cooker.Name, "made and outstanding meal of", Food_Item.Name, ". It's excellent quality.")

    if Food_Item.COOK_EATABLE is False and (Cooker.Naturalist[0] > 9 or (Cooker.Science[0] > (11 - (Cooker.ANA/3 - Cooker.PE/3)) and "Biology" in Cooker.Science[1] is True)):
        if Food_Item.RAW_EATABLE is True:
            print("But you notice that this is uneatable now and can only be eaten raw.")
        else:
            print("But you notice that this is still uneatable.")

    if Food_Item.POISONOUS[0] is True and S > (10 - Cooker.ANA/2 - Cooker.PE/2):
        print("You also find out that", Food_Item.Name, "is poisonous to", Food_Item.POISONOUS[1])

    if S < 0:
        rd.randint(1,100)
        if Food_Item.FLAMMABLE is True and roll >= 1 and roll < 20:
            if S >= -4 and S < 0:
                print(Cooker.Name,"burnt the", Food_Item.Name, "but it still eatable. It's poor quality.")
            elif S >= -9 and S < -4:
                print(Cooker.Name, "burn the", Food_Item.Name, "to a crisp. It's uneatable.")
            elif S < -9:
                print(Cooker.Name, "set the food on fire!", Food_Item.Name, "is uneatable and in flames.")

        if Food_Item.MOIST is True and roll >= 20 and roll < 51:
            if S >= -4 and S < 0:
                print(Food_Item.Name, "have dried out. Now it's poor quality.")
            elif S < -4:
                print(Food_Item.Name, "have dried out and is completely spoiled. Now it's uneatable.")

        else:
            if S >= -5 and S < 0:
                print(Cooker.Name, "made a bad meal.", Food_Item.Name, "is poor quality.")
            elif S < -5:
                print(Cooker.Name, "made a horrible meal.", Food_Item.Name, "is uneatable.")

def Repair(character = char.Char(), target = item.Item, personal = 0, familiarity = 0, technology = 0, extra_against = 0,
    extra_for = 0, difficulty = 0, skill = "Repair"):

    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Repairer = character
    Target = target

    Rating = list_i[dict_i[skill]]
    Personal = personal ### Enter Personality and Emotional Factors (p)
    Familiarity = familiarity ### How well they know the recipe (f)
    Technology = technology ### Quality of the Technology (t)
    Extra_Against = extra_against ### Any Additional Factors (e_n)
    Extra_For = extra_for ### Any Additional Factors (e_d)

    Difficulty = difficulty

    S = ((Rating + Personal) * round(rd.uniform(0.90,1.10), 2)) - (Difficulty * ((1 + Extra_Against) / (1 + Familiarity * Technology
    * Extra_For)))

    print(S)

    if S >= 0:
        Repaired = Target.Damage[0] - S*10
        Target.Damage[0] = Repaired
        if Repaired <= 0:
            print(Target.Name, "has been repaired", abs(Repaired), "damage.")
        else:
            print(Target.Name, "has been damaged by", abs(Repaired), "amount.")

    #!/usr/bin/env python
    else:
        Repaired = Target.Damage[0] - S*2
        Target.Damage[0] = Repaired
        print(Target, "has been damaged by", Repaired, "amount.")

def Artist(character = char.Char(), personal = 0, familiarity = 0, technology = 0, extra_against = 0,
    extra_for = 0, difficulty = 0, cultures_amount = 1, time = 1, assistance = 0, budget = 1,
    budget_requirement = 100, viewers = [5], skill = "Repair"):

    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Artist = character

    Rating = list_i[dict_i[skill]]


    Personal = personal ### Enter Personality and Emotional Factors (p)
    Familiarity = familiarity
    Technology = technology
    Extra_Against = extra_against ### Any Additional Factors (e_n)
    Extra_For = extra_for ### Any Additional Factors (e_d)

    Viewers = viewers ### From 1 to 10, how much do they like art the artist is creating. Put a number for each group of viewers
    Cultures = cultures_amount ### How many cultures are there amoung the viewers
    Group = sum(Viewers)/Cultures ### Add the cultural difference of the artist and the viewers. x_! is each viewers and y is the number of cultures.

    Time = time ### How many time spend in 1 every 24 hours on the piece of work?
    Assistance = assistance ### How many people are working at the project.
    Budget = budget ### Amount of money in the project
    Size = budget_requirement ### How big is the project? How much have to be spent to start this project of this quality Example: AAA is $100,000,000

    Difficulty = 4 + Cultures
    Cal_i = eg.Minner(Budget/Size, 0, 2)
    Cal_ii = eg.Minner(Time/(3650/Assistance), -400, 3)

    S = ((Rating + Personal) * round(rd.uniform(0.90, 1.10))) - (Difficulty * ((1 + Extra_Against + Group)/(1 + Extra_For +
    Familiarity + Technology + Cal_i + Cal_ii)))

    print(S)

    if S < -19:
        print(Artist.Name, Skill, "was one of the worst works of art of all times. It will be remembered as an abomination of the arts. It's a 1/10")

    elif S >= -19 and S < -13:
        print(Artist.Name, Skill, "is a terrible work of art. It will get an infamous status among the arts. It's a 2/10")

    elif S >= -13 and S < -8:
        print(Artist.Name, Skill, "is isn't a great piece of work, could have been much more. It's a 3/10")

    elif S >= -8 and S < -4:
        print(Artist.Name, Skill, "is a bleak piece of work. It's a 4/10")

    elif S >= -4 and S < 0:
        print(Artist.Name, Skill, "is medicore. Forgettable. It's a 5/10")

    elif S >= 0 and S < 5:
        print(Artist.Name, Skill, "is okay, passible. It's a 6/10")

    elif S >= 5 and S < 11:
        print(Artist.Name, Skill, "is a good piece of work, something people will comeback too. It's a 7/10")

    elif S >= 11 and S < 15:
        print(Artist.Name, Skill, "is a great piece of work, it will be known in as a mark in the history of the arts. It's a 8/10")

    elif S >= 15 and S < 20:
        print(Artist.Name, Skill, "is an outstanding work of art, a milestone in the development of the arts. It's a 9/10")

    elif S >= 20:
        print(Artist.Name, Skill, "is one of the greatest works of art of all time, it has revoultionized the entire artscape of its field, created a cultural shift. It's a 10/10")

def Navigating(character = char.Char(), direction = 0, speed = 0, personal = 0, familiarity = 0, technology = 0, extra_against = 0,
    extra_for = 0, accuracy = 0, difficulty = 0, skill = "Cylaxian"):

    dict_i = {"Acrobatics":0, "Aerobatics":1, "Aiding":2, "Aquabatics":3, "Arm_Combat":4, "Art":5, "Attack":6, "Chemistry":7,
                "Climbing":8, "Cooking":9, "Cylaxian":10, "Diplomacy":11, "Disguise":12, "Electrician":13,
                "Electronic_Operation":14, "Engineering":15, "Fast_Draw":16, "Games":17, "Guns":18, "Hobby":19, "Math":20,
                "Melee_Weapon":21, "Navigation":22, "Naturalist":23, "Physics":24, "Repair":25, "Science":26, "Stealth":27,
                "Strategy":28, "Suit":29, "Tactics":30, "Vehicle":31, "Writing":32}

    list_i = [character.Acrobatics[0], character.Aerobatics[0], character.Aiding[0], character.Aquabatics[0],
                character.Arm_Combat[0], character.Art[0], character.Attack[0], character.Chemistry[0], character.Climbing[0],
                character.Cooking[0], character.Cylaxian[0], character.Diplomacy[0], character.Disguise[0],
                character.Electrician[0], character.Electronic_Operation[0], character.Engineering[0], character.Fast_Draw[0],
                character.Games[0], character.Guns[0], character.Hobby[0], character.Math[0], character.Melee_Weapon[0],
                character.Navigation[0], character.Naturalist[0], character.Physics[0], character.Repair[0], character.Science[0],
                character.Stealth[0], character.Strategy[0], character.Suit[0], character.Tactics[0], character.Vehicle[0],
                character.Writing[0]]

    Navigator = char.Char()
    Direction = direction ### 0 North, 90 East, 180 South, 270 West
    Speed = speed

    Familiarity = familiarity
    Technology = technology
    Extra_Against = extra_against
    Extra_For = extra_for

    Rating = list_i[dict_i[skill]]
    Personal = personal

    Difficulty = difficulty
    Vision = vision

    S = (((Rating + Personal + Accuracy) * round(rd.uniform(Cal_i.result, 1.10), 2) -
    (Difficulty * ((1 + Vision + Extra_Against ) / (1 + Familiarity + Technology + Extra_For)))))

    if S > 0:
        if S >= 12 - Technology:
            print("You know where you are going. You move as desired.")
        elif S < 12 - Technology:
            miss_meters = round(Speed*rd.uniform(0.85,1.00), 2)
            misdirection = eg.Random_Direction(int(Direction-(S*5)), int(Direction+(S*5)))
            print("You are heading the right direction, but you move", miss_meters, "towards", misdirection.Final_Direction)

    else:
        if S <= -1 and S >= -4:
            print("You couldn't get a good read. You don't know where to go.")
        else:
            miss_meters = round(Speed*rd.uniform(0.85,1.00), 2)
            misdirection = eg.Random_Direction(int((Direction-40)-(S*5)), int((Direction+40)+(S*5)))
            print("You move, but realize that you are lost. You move", miss_meters, "at", misdirection.Final_Direction)

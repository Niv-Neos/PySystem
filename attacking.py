import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

import character_sheet as char
import character_sheet as defender
import advance_attacks as aa
import basic_attacks as ba
import weapon_attacks as wa
import character_sheet as protect
import weapons as wp

def Attacking(
char_att = char.Char(),
char_def = defender.Char(),
attack = ba.Attack(),
protect = defender.Char(),
additional_dr = 0,
external_effect = eg.Empty(),
familiarity = 0,
technology = 0,
rating = skill_att[0] + 6,
personal = 0,
accuracy = 0,
extra_against = 0,
extra_for = 0,
cover = 0,
vision = 0,
range = 0,
hit_zone = 0,
inability = 0,
difficulty = abs(5 + skill_def[0] + Hit_Zone - Inability),
preperation = 0
):


    Attacker = char_att
    Defender = char_def
    Attack = attack ### Weapons need to be called
    Protection = protect

    Additional_DR = additional_dr

    External_Effect = eg.Empty()

    Familiarity = familiarity
    Technology = technology

    Rating = rating
    Personal = personal
    Accuracy = accuracy
    Extra_Against = extra_against
    Extra_For = extra_for
    Cover = cover
    Vision = vision
    Range = range

    Hit_Zone = hit_zone
    Inability = inability
    Difficulty = difficulty
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

    Cal_i = eg.Minner((Accuracy/20) + 0.60, 0.60, 1.20)
    Cal_ii = eg.Minner((Preperation/20) + 0.60, 0.60, 1.20)

    S = round((((Rating + Personal + Accuracy) * round(rd.uniform(Cal_i.result, 1.20), 2) -
    (Difficulty * ((1 + Cover + Damage + Vision + Range + Extra_Against ) / (1 + Familiarity + Technology + Extra_For))
    * round(rd.uniform(Cal_ii.result, 1.20), 2)))), 2)

    print(S)

    if S > 0:
        Attack.Effect(Attacker, Defender, Attack, Protection, Additional_DR, External_Effect)

    else:
        print("You miss the target.")

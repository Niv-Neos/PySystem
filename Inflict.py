import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

### Import the Character here
import character_sheet as char

Success = S
Attacker = char.Char()
Attack =

Rating = Attacker.{Insert} ### (r)
Personal = ### Enter Personality and Emotional Factors (p)
Accuracy = ### Acc (a)
Extra_Against = ### Any Additional Factors (e_n)
Extra_For = ### Any Additional Factors (e_d)
Cover = ### Cover of the Target (c)
Vision = ### How well can they see the target (v)
Range = ### In Meters (g)

Difficulty = 0 ### (d)

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

Add bonuses and penalities if they are abnormally larger or shorter than the body.
'''

Damage = sum(Attacker.Damage[0]/((Attacker.Height/33) + (Attacker.Width/33) + (Attacker.Length/33) + ((Attacker.CO)*10)), (Attacker.Damage[1]/10) * (Attacker.Weight/100) / ((Attacker.HT)*10),
Attacker.Damage[2]/(Attacker.WIL*10), Attacker.Damage[3]/50+(Attacker.WIL*5), Attacker.Damage[4]/50+(Attacker.WIL*5), Attacker.Damage[5]/50+(Attacker.WIL*5)) ### Damage on the attacker(m)

Familiarity = ### How well they know the recipe (f)
Technology = ### Quality of the Technology (t)

S = (((Rating + Personal + Accuracy) * round(rd.randint(( Accuracy/100) + 0.6, 1.2), 2) -
(Difficulty * (1 + ( Cover + Damage + Vision + Range + Extra_Against ) / (Familiarity * Technology * Extra_For) ) ))

print(S)

if S > 0:
    print("You hit the target! They are inflicted", {Insert}, "from the action.")

else:
    print("You miss the target.")

import math as mt
import numpy as np
import random as rd
import engine as eg

### Import the Character here
import character_sheet as char
import character_sheet as defender
import basic_attacks as attack
import character_sheet as protect

Attacker = char.Char()
Defender = defender.Char()
Attack = attack.Pheromone_Spray()
Protection = protect.Char()

Familiarity = 1
Technology = 3

Rating = Attacker.Arm_Combat[0] + 6 ### (r)
Personal = 1 ### Enter Personality and Emotional Factors (p)
Accuracy = 4 ### Acc (a)
Extra_Against = 1 ### Any Additional Factors (e_n)
Extra_For = 2 ### Any Additional Factors (e_d)
Cover = 0 ### Cover of the Target (c)
Vision = 1 ### How well can they see the target (v)
Range = 1 ### In Meters (g)

Hit_Zone = 0
Difficulty = 5 + Defender.Arm_Combat[0] + Hit_Zone ### (d)

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
Torso (0)

Add bonuses and penalities if they are abnormally larger or shorter than the body.
'''

Damage = ((Attacker.Damage[0]/((Attacker.Height/33) + (Attacker.Width/33) + (Attacker.Length/33) + ((Attacker.CO)*10)))) + ((Attacker.Damage[1]/10) * (Attacker.Weight/100) / ((Attacker.HT)*10))
+ (Attacker.Damage[2]/(Attacker.WIL*10)) + (Attacker.Damage[3]/(Attacker.WIL*10)) + (Attacker.Damage[4]/(Attacker.WIL*10)) + (Attacker.Damage[5]/(Attacker.WIL*10)) ### Damage on the attacker(m)

Familiarity = 3
Technology = 3 ### Quality of the Technology (t)

Cal_i = eg.Minner((Accuracy/100) + 0.60, 0.60, 1.20)

S = round((((Rating + Personal + Accuracy) * round(rd.uniform(Cal_i.result, 1.20), 2) -
(Difficulty * (1 + ( Cover + Damage + Vision + Range + Extra_Against ) / (Familiarity + Technology + Extra_For) )))), 2)

print(S)

if S > 0:
    Attack.Effect(Attacker, Defender, Attack, Protection)

else:
    print("You miss the target.")

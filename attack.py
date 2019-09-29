import math as mt
import numpy as np
import random as rd

### Import the Character here
import character_sheet as char

Success = S
Cooker = char.Char()

Rating = Cooker.Cooking ### (r)
Personal = ### Enter Personality and Emotional Factors (p)
Accuracy = ### Acc (a)
Extra_Against = ### Any Additional Factors (e_n)
Extra_For = ### Any Additional Factors (e_d)
Cover = ### Cover of the Target (c)
Vision = ### How well can they see the target (v)
Range = ### In Meters (g)

Difficulty = 0 ### (d)

Damage = ### Damage on the attacker(m)

Familiarity = ### How well they know the recipe (f)
Technology = ### Quality of the Technology (t)

S = ((Rating + Personal + Accuracy) * rd.randint( ( Accuracy/100) + 0.6,1.2 ) ) - (Difficulty * (1 + ( Cover + Damage + Vision + Range + Extra_Against ) / (Familiarity * Technology * Extra_For) ) )

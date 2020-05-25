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
import common_items as item

Repairer = char.Char()
Target = item.Item()

Rating = Repairer.Repair[0] ### (r)
Skill = Repairer.Repair[1]
Personal = 2 ### Enter Personality and Emotional Factors (p)
Extra_Against = 1 ### Any Additional Factors (e_n)
Extra_For = 2 ### Any Additional Factors (e_d)

Difficulty = Target.Damage[0]/10 ### (d)

Familiarity = 3 ### How well they know the recipe (f)
Technology = 1 ### Quality of the Technology (t)

S = ((Rating + Personal) * round(rd.uniform(0.90,1.10), 2)) - (Difficulty * ((1 + Extra_Against) / (1 + Familiarity * Technology * Extra_For)))

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

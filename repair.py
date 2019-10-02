import math as mt
import numpy as np
import random as rd
import engine as eg

### Import the Character here
import character_sheet as char
import common_items as item

Success = S
Repairer = char.Char()
Target = item.Item()

Rating = Cooker.Repair[0] ### (r)
Skill = Cooker.Repair[1]
Personal = ### Enter Personality and Emotional Factors (p)
Extra_Against = ### Any Additional Factors (e_n)
Extra_For = ### Any Additional Factors (e_d)

Difficulty = Target.Damage[0]/10 ### (d)

Familiarity = ### How well they know the recipe (f)
Technology = ### Quality of the Technology (t)

S = ((Rating + Personal) * round(rd.uniform(0.90,1.10), 2)) - (Difficulty * (1 + Extra_Against / (Familiarity * Technology * Extra_For)))

print(S)

if S >= 0:
    Repaired = Target.Damage[0] - S*10
    Target.Damage[0] = Repaired
    if Repaired >= 0:
        print(Target, "has been repaired", Repaired, "damage.")
    else:
        print(Target, "has been damaged by" Repaired, "amount.")

#!/usr/bin/env python
else:
    Repaired = Target.Damage[0] - S*2
    Target.Damage[0] = Repaired
    print(Target, "has been damaged by" Repaired, "amount.")

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

Skill_User = char.Char()

Rating = char.{}[0]

Familiarity =
Technology =
Extra_Against =
Extra_For =

Cal_i = eg.Minner(var = , min = , max = )

S = round((Rating + Personal + Accuracy) * round(rd.uniform(0.80, 1.20), 2) -
(Difficulty * ((1 + Extra_Against) / (1 + Familiarity + Technology + Extra_For))), 2)

print(S)

if S > 0:
    print(Skill_User.Name, "succeed the challenge.")

elif S <= 0:
    print(Skill_User.Name, "failed the challenge.")

else:
    print("Something have went wrong. Most likely due to S not being a float.")

import math as mt
import numpy as np
import random as rd
import engine as eg

import character_sheet as char

Skill_User = char.Char()

Rating = char.{}[0]

Familiarity =
Technology =
Extra_Against =
Extra_For =

Cal_i = eg.Minner(var = , min = , max = )

S = round(((Rating + Personal + Accuracy) * roundrd.uniform((0.80, 1.20)), 2) -
(Difficulty * (1 + (Extra_Against) / (Familiarity + Technology + Extra_For))), 2)

print(S)

if S > 0:
    print(Skill_User.Name, "succeed the challenge.")

if S < 0:
    print(Skill_User.Name, "failed the challenge.")

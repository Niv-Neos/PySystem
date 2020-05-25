import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import technology_function as tf
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

import character_sheet as char

Builder = char.Char()

Rating = char.{}[0]

Familiarity =
Technology =
Tools = tf.BuildingTools(self, tools = False, pullers = False, vehicles = False, additive = False,
                        interlock = False, magnetism = False, cylax = False)
Extra_Against =
Extra_For =
Building_Progress = ### In Precentage
Time_Spent = 0 ### In Minutes
Structure_Volume = ### In Metrics Cubic

Cal_i = eg.Minner(var = Building_Progress, min = 0, max = 100)

S = round((Rating + Personal + Accuracy) * round(rd.uniform(0.80, 1.20), 2) -
(Difficulty * ((1 + Extra_Against) / (1 + Familiarity + Technology + Extra_For))), 2)

New_Progress = (S * (1 + Technology / 2) * Tools.result) * (Time_Spent / 60) / Structure_Volume
Building_Progress = Building_Progress + New_Progress
Building_Progress = Cal_i.result

print(S)

if S > 0:
    print(Builder.Name, "have made progress.")
    print("After", Time_Spent,",", Builder.Name, "made", New_Progress, "change, now it's at", Building_Progress, "progress.")
    print("The object is now", Building_Progress, "% complete.")
    if Building_Progress == 100:
        print("The object is finished.")
    else:
        info = 100 - Building_Progress
        print("The object is", info, "% away to being finished.")

elif S < 0 and S >= -8:
    print(Builder.Name, "you didn't made any progress .")
    print("After", Time_Spent,",", Builder.Name, "made 0 change, now it's at", Building_Progress, "progress.")

elif S < 8:
    print(Builder.Name, "have reduce progress.")
    print("After", Time_Spent,",", Builder.Name, "made", New_Progress, "change, now it's at", Building_Progress, "progress.")
    print("The object is now", Building_Progress, "% complete.")
    if Building_Progress == 100:
        print("The object is finished.")
    else:
        info = 100 - Building_Progress
        print("The object is", info, "% away to being finished.")

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

Navigator = char.Char()
Direction = 90 ### 0 North, 90 East, 180 South, 270 West
Speed = 5

Familiarity = 1
Technology = 2
Extra_Against = 1
Extra_For = 1
Accuracy = 3

Rating = Navigator.Navigation[0]
Personal = 1

Difficulty = 1
Vision = 0

Cal_i = eg.Minner((Accuracy/20) + 0.80, 0.80, 1.10)

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

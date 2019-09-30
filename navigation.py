import math as mt
import numpy as np
import random as rd
import engine as eg

import character_sheet as char

Success = S
Navigator = char.Char()
Direction = eg.Minner({Insert}, -0.1, 360.1) ### 0 North, 90 East, 180 South, 270 West
Speed = 0

Rating = char.Navigation_Skill[0]

Cal_i = eg.Minner((Accuracy/100) + 0.80, 0.80, 1.10)

S = (((Rating + Personal + Accuracy) * round(rd.uniform((Cal_i.result, 1.10)), 2) -
(Difficulty * (1 + ( Vision + Extra_Against ) / (Familiarity * Technology * Extra_For) ) ) )

if S > 0:
    if S >= 12 - Technology:
        print("You know where you are going. You move as desired.")
    if S < 12 - Technology:
        miss_meters = Speed*round((rd.uniform(0.85,1.00)), 2)
        eg.random_direction(rd.random((Direction)+(S*5), (Direction)-(S*5)))
        print("You are heading the right direction, but you move", miss_meters, "towards", misdirection)

if S < 0:
    if S <= -1 and S >= -4:
        print("You couldn't get a good read. You don't know where to go.")
    else:
        lost_meters = Speed*round(rd.uniform(0.85,1.00), 2)
        eg.random_direction(rd.random((Direction-40)+(S*5), (Direction+40)-(S*5)))
        print("You move, but realize that you are lost. You move", lost_meters, "at", lost_direction)

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
Artist = char.Char()

Rating = Artist.{Insert}[0]
Skill = Arist.{Insert}[0]

Familiarity =
Technology =

Personal = ### Enter Personality and Emotional Factors (p)
Extra_Against = ### Any Additional Factors (e_n)
Extra_For = ### Any Additional Factors (e_d)

Viewers = [] ### From 1 to 10, how much do they like art the artist is creating. Put a number for each group of viewers
Cultures =  ### How many cultures are there amoung the viewers
Group = sum(Viewers)/Cultures ### Add the cultural difference of the artist and the viewers. x_! is each viewers and y is the number of cultures.

Time = ### How many time spend in 1 every 24 hours on the piece of work?
Assistance = ### How many people are working at the project.
Budget = ### Amount of money in the project
Size = ### How big is the project? How much have to be spent to start this project of this quality Example: AAA is $100,000,000

Difficulty = 4 + Cultures
Cal_i = eg.Minner(Budget/Size, 0, 2)
Cal_ii = eg.Minner(Time/(3650/Assistance), -400, 3)

S = ((Rating + Personal) * round(rd.uniform(0.90, 1.10))) - (Difficulty * ((1 + Extra_Against + Group)/(1 + Extra_For + Familiarity + Technology + Cal_i + Cal_ii)))

print(S)

if S < -19:
    print(Artist.Name, Skill, "was one of the worst works of art of all times. It will be remembered as an abomination of the arts. It's a 1/10")

elif S >= -19 and S < -13:
    print(Artist.Name, Skill, "is a terrible work of art. It will get an infamous status among the arts. It's a 2/10")

elif S >= -13 and S < -8:
    print(Artist.Name, Skill, "is isn't a great piece of work, could have been much more. It's a 3/10")

elif S >= -8 and S < -4:
    print(Artist.Name, Skill, "is a bleak piece of work. It's a 4/10")

elif S >= -4 and S < 0:
    print(Artist.Name, Skill, "is medicore. Forgettable. It's a 5/10")

elif S >= 0 and S < 5:
    print(Artist.Name, Skill, "is okay, passible. It's a 6/10")

elif S >= 5 and S < 11:
    print(Artist.Name, Skill, "is a good piece of work, something people will comeback too. It's a 7/10")

elif S >= 11 and S < 15:
    print(Artist.Name, Skill, "is a great piece of work, it will be known in as a mark in the history of the arts. It's a 8/10")

elif S >= 15 and < 20:
    print(Artist.Name, Skill, "is an outstanding work of art, a milestone in the development of the arts. It's a 9/10")

elif S >= 20:
    print(Artist.Name, Skill, "is one of the greatest works of art of all time, it has revoultionized the entire artscape of its field, created a cultural shift. It's a 10/10")

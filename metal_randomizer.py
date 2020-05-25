import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

volume = 100 ### in m
O = 0
OR = range(1,47)
Si = 0
SiR = range(48,74)
Al = 0
AlR = range(75,82)
Fe = 0
FeR = range(83,88)
Ca = 0
CaR = range(89,94)
Na = 0
NaR = range(95,97)
K = 0
KR = range(98,99)
Ti = 0
TiR = range(100,101)
H = 0
HR = range(102,103)
Other = 0
OtherR = range(104,105)
while volume != 0:
    c = random.randint(1,105)
    print(volume)
    if c == range(1,47):
         O = O + 1
         volume = volume - 1
    elif c == range(48,74):
         Si = Si + 1
         volume = volume - 1
    elif c == range(75,82):
         Al = Al + 1
         volume = volume - 1
    elif c == range(83,88):
         Fe = Fe + 1
         volume = volume - 1
    elif c == range(89,94):
         Ca = Ca + 1
         volume = volume - 1
    elif c == range(95,97):
         Na = Na + 1
         volume = volume - 1
    elif c == range(98,99):
         K = K + 1
         volume = volume - 1
    elif c == range(100,101):
         Ti = Ti + 1
         volume = volume - 1
    elif c == range(102,103):
         H = H + 1
         volume = volume - 1
    elif c == range(104,105):
         Other = Other + 1
         volume = volume - 1
while volume == 0:
    print("Oxygen: ",O)
    print("Silicon: ",Si)
    print("Aluminium: ",Al)
    print("Iron: ",Fe)
    print("Calcium: ",Ca)
    print("Sodium: ",Na)
    print("Potassium: ",K)
    print("Magnesium: ",Ti)
    print("Titanium: ",Ti)
    print("Hydrogen: ",H)
    print("Others: ",Other)

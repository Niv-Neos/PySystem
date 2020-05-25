import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Race:

    def __init__(self, speed = 0, analytical = 0, creative = 0, emotion = 0, will = 0, strength = 0, dexterity = 0,
                    constitution = 0, health = 0, perception = 0, hp = 0, fp = 0, mp = 0, sanity = 0, lust = 0, fear = 0,
                    dodge = 0, move = 0, dr = 0, flammable = False, poisonous = [False, []], raw_eatable = False,
                    cook_eatable = False, moist = False, name = "", type = "Biological", discription = "", sextype = "Tyromitive"):

        self.Name = name
        self.Type = type
        self.Discription = discription

        self.SPEstat = speed
        self.ANAstat = analytical
        self.CREstat = creative
        self.EMOstat = emotion
        self.WILstat = will

        self.STstat = strength
        self.DXstat = dexterity
        self.COstat = constitution
        self.HTstat = health
        self.PEstat = perception

        ### Base Secondary

        self.HPstat = hp
        self.FPstat = fp
        self.MPstat = mp

        self.Sanitystat = sanity
        self.Luststat = lust
        self.Fearstat = fear

        self.Dodgestat = dodge
        self.Movestat = move

        self.DRstat = dr

        self.FLAMMABLE = flammable
        self.POISONOUS = poisonous ### Apply to what
        self.RAW_EATABLE = raw_eatable
        self.COOK_EATABLE = cook_eatable
        self.MOIST = moist

        self.SEXTYPE = sextype

Species_Test = Race(
speed = 0,
analytical = 0,
creative = 0,
emotion = 0,
will = 0,
strength = 0,
dexterity = 0,
constitution = 0,
health = 0,
perception = 0,
hp = 0,
fp = 0,
mp = 0,
sanity = 0,
lust = 0,
fear = 0,
dodge = 0,
move = 0,
dr = 0,
flammable = False,
poisonous = [False, []],
raw_eatable = False,
cook_eatable = False,
moist = False,
name = "",
type = "Biological",
discription = "",
sextype = "Tyromitive"
)

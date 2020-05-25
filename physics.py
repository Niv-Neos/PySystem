import math as mt
import numpy as np
import random as rd
import engine as eg
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem/Characters')

import character_sheet as char
import realm as re
#
world = re.Realm()

class Teeth_Change:
    def __init__(self, character):
        while "Weak Bite" in character.Traits:
            num_i = 0.5
        else:
            num_i = 1
        self.Result = num_i

class Force:
    def __init__(self, num_i):
        self.Force = num_i
        self.Knockback = num_i
        self.Knockup = num_i
        self.Push = num_i
        self.Pull = num_i

class Electrical_Charge:
    def __init__(self, current, resistance, time = 1):
        ### Time is in seconds
        self.pressure = current * resistance
        self.power = self.pressure * current
        self.energy = self.power * time
        self.heat = (current**2) * resistance * time

class Floor_Area():

    def __init__(self, floortype, character):
        dict_i = {"Dirt":1, "Water":0.5, "Cement":2, "Ring Floor":0.2}
        self.Weight = (character.Volume * 0.66) * dict_i[floortype]

def Falling(object, mechanical_gravity, time):
    d = 0.5 * mechanical_gravity * (time**2)
    print("After", time, "seconds,", object.Name, "falls", d, "meters.")

def Burning_Damage(character, fire = 0, area = 1, temp_o = 600, temp_c = 310.15, freq = 0, rad = 0, rng = 1, material = "animal"):
    ### Fire = 0, Plasma = 1, Hot = 2, Microwave = 3, Ionizing = 4
    ### Area is in metrics^2
    ### num_i = Damage, num_ii = Radiation
    if fire == 0:
        Cal_i = eg.Minner((area*(temp_o-temp_c)/10), 1, character.Volume/60)
        num_i = Cal_i.result
        check_i = False
        index = 0
    elif fire == 1:
        Cal_i = eg.Minner((area*(temp_o-temp_c)/7.5), 1, character.Volume/60)
        num_i = Cal_i.result
        check_i = False
        index = 1
    elif fire == 2:
        Cal_i = eg.Minner((area*(temp_o-temp_c)/10), 1, character.Volume/60)
        num_i = Cal_i.result
        check_i = False
        index = 2
    elif fire == 3:
        Cal_i = eg.Minner((area*freq)-rng/10, 1, character.Volume/60)
        num_i = Cal_i.result
        check_i = True
        index = 3
    elif fire == 4:
        Cal_i = eg.Minner(((area*rad)/rng)/10, 1, character.Volume/60)
        num_i = Cal_i.result
        check_i = True
        index = 4
    else:
        print("Not a vaild fire type. Fire = 0, Plasma = 1, Hot = 2, Microwave = 3, Ionizing = 4")
    '''
    list_i = ["Causes objects to ignite in flames", "Causes Normal Damage.", "Causes Normal Damage.", "Causes Normal Damage.", "Causes Normal Damage."]
    list_ii = ["water", "metal", "plant", "animal", "fabric", "oil"]
    '''

    dict_i = {"water":0, "matel":0.2, "plant":2, "animal":1, "fabric":4, "oil":8}
    list_i = [0, 0.2, 2, 1, 4, 8]

    Damage = round(num_i * dict_i[material], 2)
    Radiation = check_i

    Burning_Effect = list_i[index]

    character.Damage[0] = round(character.Damage[0] + Damage, 2)
    print(character.Name, "take", Damage, "burning damage. Now they have", character.Damage[0], "HP damage.")
    if fire == 0:
        print("All hit objects are in flames if able.")
        Continuous_Flames(character, temp_o, area, material)

def Continuous_Flames(object, temp_f = 600, area = 1, material = "animal"):
    if material is "metal":
        num_i = mt.ceil((object.HP*object.Volume)/600/1000)
        num_ii = 300
    if material is "plant":
        num_i = mt.ceil((object.HP*object.Volume)/600/100)
        num_ii = 100
    if material is "animal":
        num_i = mt.ceil((object.HP*object.Volume/600)/200)
        num_ii = 200
    if material is "water":
        num_i = 0
        num_ii = 1000
    if material is "fabric":
        num_i = mt.ceil((object.HP*object.Volume/600)/50)
        num_ii = 100
    if material is "oil":
        num_i = mt.ceil((object.HP*object.Volume/600)/10)
        num_ii = 100
    Damage = round(temp_f/(object.Volume/100), 2)
    Time = num_i/num_ii
    print(object.Name, "is on fire for", mt.floor(Time), "turns, taking", Damage, "HP damage each turn.")

def Freezing_Damage(character, temp_o = 273.15, temp_c = 310.15):
    Damage = mt.floor(area*((temp_c+character.CO)-temp_o)/20)
    Penalty = mt.floor((area*((temp_c+character.CO)-temp_o))/50)
    character.Damage[0] = round(character.Damage[0] + Damage)
    print(character.Name, "take", Damage, "frost damage. Now they have", character.Damage[0], "HP damage.")
    print(character.Name, "suffers", -Penalty/5, "penality to ST and DX for", (Penalty-character.CO), "turns.")

def Collision(object_i, object_ii, move_i, move_ii):
    Gravity = 1 * cf.world.Mechanical_gravity
    dealt_i = ((((object_i.Weight/2) + object_ii.Weight)/20) * Gravity) + ((((move_i/2) + move_ii)/20) * Gravity)
    dealt_ii = (((object_i.Weight + (object_ii.Weight/2))/20) * Gravity) + (((move_i + (move_ii/2))/20) * Gravity)
    object_i.Damage[0] = round(object_i.Damage[0] + dealt_i, 2)
    object_ii.Damage[0] = round(object_i.Damage[0] + dealt_ii, 2)
    print(object_i.Name, "and", object_ii.Name, "collide.")
    print(object_i.Name, "is dealt", dealt_i, "damage.")
    print(object_ii.Name, "is dealt", dealt_ii, "damage.")


def Knockback(attack, defender):
    Gravity = 1 * world.Mechanical_gravity
    Knockback = (attack.Knockback) / (defender.Weight * (world.Mechanical_gravity + (1.0*(10**-11))))
    print(defender.Name, "is Knockback", Knockback, "meters.")

def Impregnation_Check(character_r, character_g, seeding_type, protection):
    ### Seeding Types: Sex, Hand In, Injection
    if "Sterile" in character_r.Traits or "Sterile" in character_g.Traits:
        print("You do not get pregnated.")
        if prodection is True:
            num_i = 0.01
            return
        else:
            num_i = 1
            return
        num_ii = rd.randint(-10,4)
        num_iii = character_r.HT + 4
        num_iv = character_g.HT + 4
        if seeding_type == "Sex":
            num_v = 1
            return
        elif seeding_type == "Hand In":
            num_v = 0.3
            return
        elif seeding_type == "Injection":
            num_v = 2
            return
        Result = (num_ii + num_iii + num_iv) * num_i * num_v
        if Result >= 20:
            print("You have successifully got pregnated.")
        else:
            print("You do not get pregnated.")

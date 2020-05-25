import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

import kan_species as race ### Insert Species at Race
Kan = race.Kan()

class Char:

    def __init__(self, speed = 10, analytical = 10, creative = 10, emotional = 10, will = 10, strength = 10, dexterity = 10,
    constitution = 10, health = 10, perception = 10, height = 120, width = 40, length = 33, weight = 20, dr = 0, acrobatics_skill = 0,
    aerobatics_skill = 0, aiding_skill = 0, aquabatics_skill = 0, arm_combat_skill = 0, art_skill = 0, attack_skill = 0,
    chemistry_skill = 0, climbing_skill = 0, cooking_skill = 0, cylaxian_skill = 0, diplomacy_skill = 0, disguise_skill = 0,
    electrician_skill = 0, electronic_operation_skill = 0, engineering_skill = 0, fast_draw_skill = 0, games_skill = 0,
    guns_skill = 0, hobby_skill = 0, math_skill = 0, melee_weapon_skill = 0, navigation_skill = 0, naturalist_skill = 0,
    physics_skill = 0, repair_skill = 0, science_skill = 0, stealth_skill = 0, strategy_skill = 0, suit_skill = 0, tactics_skill = 0,
    vehicle_skill = 0, writing_skill = 0, gender = "", name = "character", race = Kan, languages = {"English":3},
    damage = [0,0,0,0,0,0,0], arms = True, legs = True, wings = False, sight = True, hearing = True, feeling = True, taste = True,
    smell = True, viberation = False, poisoned = None, pregnate = [False, 0, 0], unconscious = False, broken_arms = [False, 0],
    broken_legs = [False, 0], dazed = False, short_curcuit = False, broken_wings = [False, 0], familiarities = {"":0}, traits = ["Claw"],
    effects = [""], cylax_tech = {"Carbon Life":-1}, cylax_value = bin(0), items = [""], arm_combat_list = {"":0}, art_list = {"":0}, attack_list = {"":0},
    cooking_list = {"":0}, disguise_list = {"":0}, electronic_operation_list = {"":0}, engineering_list = {"":0},
    fast_draw_list = {"":0}, games_list = {"":0}, guns_list = {"":0}, hobby_list = {"":0}, math_list = {"":0}, melee_weapon_list = {"":0}, navigation_list = {"":0},
    naturalist_list = {"":0}, physics_list = {"":0}, repair_list = {"":0}, science_list = {"":0}, strategy_list = {"":0}, suit_list = {"":0}, tactics_list = {"":0},
    vehicle_list = {"":0}):

              ### Base Functions

        Race = race

        ### Identity

        self.Name = name

        ### Base Stats

        self.SPE = speed + Race.SPEstat
        self.ANA = analytical + Race.ANAstat
        self.CRE = creative + Race.CREstat
        self.EMO = emotional + Race.EMOstat
        self.WIL = will + Race.WILstat

        self.ST = strength + Race.STstat
        self.DX = dexterity + Race.DXstat
        self.CO = constitution + Race.COstat
        self.HT = health + Race.HTstat
        self.PE = perception + Race.PEstat

        self.Species = Race.Name
        self.Type = Race.Type
        self.Gender = gender

        self.Height = height ### in centimeters
        self.Width = width
        self.Length = length
        self.Volume = self.Height * self.Width * self.Length

        self.Weight = weight ### in Kilograms

        ### Base Secondary

        self.HP = (self.CO*5) + (self.ST*2.5) + (self.HT*2.5) + Race.HPstat
        self.FP = self.HT * 10 + Race.FPstat
        self.MP = self.WIL * 10 + Race.MPstat
        self.CP = 100

        self.Sanity = self.WIL * 10 + Race.Sanitystat
        self.Lust = self.WIL * 10 + Race.Luststat
        self.Fear = self.WIL * 10 + Race.Fearstat

        self.Damage = damage ### HP, FP, MP, CP, Sanity, Lust, Fear

        self.Dodge = self.DX/2 + Race.Dodgestat
        self.Move = self.DX/2 + Race.Movestat

        self.DR = dr + Race.DRstat

        ### Base Third

        self.Languages = languages ### Rating, Language

        ### Base Traits
        self.ARMS = True
        self.LEGS = True
        self.WINGS = False

        self.SIGHT = True
        self.HEARING = True
        self.FEELING = True
        self.TASTE = True
        self.SMELL = True
        self.VIBRATION = False

        ### Condition

        self.POISONED = None
        self.PREGNATE = [False,0] ### Are they pregnaut, how long, how many babies
        self.UNCONSCIOUS = False
        self.BROKEN_ARMS = False ### If so, how many, can't be greater than amount
        self.BROKEN_LEGS = False
        self.DAZED = False

        self.SHORT_CURCUIT = False
        self.BROKEN_WINGS = False

        ### Skills

        self.Acrobatics_Skill = acrobatics_skill
        self.Acrobatics = [(self.DX-5)+self.Acrobatics_Skill] ### [Rating,Species]

        self.Aerobatics_Skill = aerobatics_skill
        self.Aerobatics = [(self.DX-5)+self.Aerobatics_Skill] ### [Rating,Species]

        self.Aiding_Skill = aiding_skill
        self.Aiding = [(self.ANA-6)+self.Aiding_Skill] ### [Rating,Species]

        self.Aquabatics_Skill = aquabatics_skill
        self.Aquabatics = [(self.DX-5)+self.Aquabatics_Skill] ### [Rating,Species]

        self.Arm_Combat_Skill = arm_combat_skill
        self.Arm_Combat = [(self.DX-4)+self.Arm_Combat_Skill,arm_combat_list] ### [Rating,Speciality]

        self.Art_Skill = art_skill
        self.Art = [((self.CRE/2)-3)+((self.ANA/4)-2)+((self.EMO/4)-2)+self.Art_Skill,art_list]### [Rating, Art]

        self.Attack_Skill = attack_skill
        self.Attack = [(self.DX-3)+self.Attack_Skill] ### [Rating]

        self.Chemistry_Skill = chemistry_skill
        self.Chemistry = [(self.ANA-6)+self.Chemistry_Skill]### [Rating]

        self.Climbing_Skill = climbing_skill
        self.Climbing = [((self.ST/4)-1)+((self.HT/4)-1)+((self.DX/2)-2)+self.Climbing_Skill] ### [Rating,Species]

        self.Cooking_Skill = cooking_skill
        self.Cooking = [((self.ANA/2)-2)+((self.CRE/2)-2)+self.Cooking_Skill,[cooking_list]] ### [Rating,Speciality]

        self.Cylaxian_Skill = cylaxian_skill
        self.Cylaxian = [((self.SPE/10)-1)+((self.ANA/10)-1)+((self.CRE/10)-1)+((self.EMO/10)-1)+((self.WIL/10)-1)+self.Cylaxian_Skill] ### Rating, look down to Cylax for techs and path.

        self.Diplomacy_Skill = diplomacy_skill
        self.Diplomacy = [((self.EMO-5)+self.Diplomacy_Skill)] ### [Rating]

        self.Disguise_Skill = disguise_skill
        self.Disguise = [(self.DX-2)+(self.ANA-2)+(self.EMO-2)+self.Disguise_Skill,disguise_list]### [Rating,Species]

        self.Electrician_Skill = electrician_skill
        self.Electrician = [(self.ANA-5)+self.Electrician_Skill]### [Rating]

        self.Electronic_Operation_Skill = electronic_operation_skill
        self.Electronic_Operation = [(self.ANA-4)+self.Electronic_Operation_Skill,electronic_operation_list]### [Rating,Speciality]

        self.Engineering_Skill = engineering_skill
        self.Engineering = [(((self.ANA/2)-3)+((self.CRE/2))-3)+self.Engineering_Skill,engineering_list]### [Rating,Speciality]

        self.Fast_Draw_Skill = fast_draw_skill
        self.Fast_Draw = [(self.DX-4)+self.Fast_Draw_Skill,fast_draw_list] ### [Rating,Speciality]

        self.Games_Skill = games_skill
        self.Games = [(((self.ANA/2)-2)+((self.CRE/2)-2))+self.Games_Skill,games_list]### [Rating,Game]

        self.Guns_Skill = guns_skill
        self.Guns = [(self.DX-4)+self.Guns_Skill,guns_list]### [Rating,Weapon,Gun Type]

        self.Hobby_Skill = hobby_skill
        self.Hobby = [(((self.ANA/2)-2)+((self.CRE/2)-2))+self.Hobby_Skill,hobby_list]### [Rating,Game]

        self.Math_Skill = math_skill
        self.Math = [(self.ANA-5)+self.Math_Skill,math_list] ### [Rating,Speciality]

        self.Melee_Weapon_Skill = melee_weapon_skill
        self.Melee_Weapon = [(self.DX-4)+self.Melee_Weapon_Skill,melee_weapon_list]### [Rating,Speciality]

        self.Navigation_Skill = navigation_skill
        self.Navigation = [((self.ANA/3)-2)+((self.SPE/3)-2)+((self.PE/3)-2),navigation_list]### [Rating,Speciality]

        self.Naturalist_Skill = naturalist_skill
        self.Naturalist = [(((self.ANA/2)-3)+((self.CRE/2)-3))+self.Naturalist_Skill,naturalist_list] ### [Rating,Bio Type]

        self.Physics_Skill = physics_skill
        self.Physics = [(self.ANA-6)+self.Physics_Skill,physics_list]### [Rating,Field]

        self.Repair_Skill = repair_skill
        self.Repair = [(self.ANA-6)+self.Repair_Skill,repair_list]### [Rating,Speciality]

        self.Science_Skill = science_skill
        self.Science = [(self.ANA-5)+self.Science_Skill,science_list]### [Rating,Field]

        self.Stealth_Skill = stealth_skill
        self.Stealth = [self.Stealth_Skill] ### [Rating,Speciality]

        self.Strategy_Skill = strategy_skill
        self.Strategy = [((self.ANA/2)-3)+((self.CRE/2)-3)+self.Strategy_Skill,strategy_list] ### [Rating,Combat Situation]

        self.Suit_Skill = suit_skill
        self.Suit = [(self.DX-4)+self.Suit_Skill,suit_list] ### [Rating,Speciality]

        self.Tactics_Skill = tactics_skill
        self.Tactics = [((self.ANA/2)-3)+((self.CRE/2)-3)+self.Strategy_Skill,tactics_list] ### [Rating,Combat Situation]

        self.Vehicle_Skill = vehicle_skill
        self.Vehicle = [(self.DX-5)+self.Vehicle_Skill,vehicle_list] ### [Rating,Type]

        self.Writing_Skill = writing_skill
        self.Writing = [((self.ANA-4)+self.Writing_Skill)*(self.Languages["English"]/3)] ### [Rating] Insert Language in the brackets of self.Languages


        '''
        Insert all familiarities they know and what level.
        1 - Beginner
        2 - Interminate
        3 - Expert
        '''

        self.Familiarities = familiarities

        self.Traits = traits
        self.Effects = effects

        ### Cylax
        self.Cylax_Tech = cylax_tech ### -1 is passive.
        self.Cylax_Value = cylax_value ### It's 4 bit, meaning in range of 0 to 15

        self.Items = items

char_test = Char(
speed = 10,
analytical = 10,
creative = 10,
emotional = 10,
will = 10,
strength = 10,
dexterity = 10,
constitution = 10,
health = 10,
perception = 10,
height = 120,
width = 40,
length = 33,
weight = 20,
dr = 0,
acrobatics_skill = 0,
aerobatics_skill = 0,
aiding_skill = 0,
aquabatics_skill = 0,
arm_combat_skill = 0,
art_skill = 0,
attack_skill = 0,
chemistry_skill = 0,
climbing_skill = 0,
cooking_skill = 0,
cylaxian_skill = 0,
diplomacy_skill = 0,
disguise_skill = 0,
electrician_skill = 0,
electronic_operation_skill = 0,
engineering_skill = 0,
fast_draw_skill = 0,
games_skill = 0,
guns_skill = 0,
hobby_skill = 0,
math_skill = 0,
melee_weapon_skill = 0,
navigation_skill = 0,
naturalist_skill = 0,
physics_skill = 0,
repair_skill = 0,
science_skill = 0,
stealth_skill = 0,
strategy_skill = 0,
suit_skill = 0,
tactics_skill = 0,
vehicle_skill = 0,
writing_skill = 0,
gender = "",
name = "character",
race = race.Kan(),
languages = {"English":3},
damage = [0,0,0,0,0,0,0],
arms = True,
legs = True,
wings = False,
sight = True,
hearing = True,
feeling = True,
taste = True,
smell = True,
viberation = False,
poisoned = None,
pregnate = [False, 0, 0],
unconscious = False,
broken_arms = [False, 0],
broken_legs = [False, 0],
dazed = False,
short_curcuit = False,
broken_wings = [False, 0],
familiarities = {"":0},
traits = ["Claw"],
effects = [""],
cylax_tech = {"Carbon_Life":-1},
cylax_value = bin(0),
items = [""],
arm_combat_list = {"":0},
art_list = {"":0},
attack_list = {"":0},
cooking_list = {"":0},
disguise_list = {"":0},
electronic_operation_list = {"":0},
engineering_list = {"":0},
fast_draw_list = {"":0},
games_list = {"":0},
guns_list = {"":0},
hobby_list = {"":0},
math_list = {"":0},
melee_weapon_list = {"":0},
navigation_list = {"":0},
naturalist_list = {"":0},
physics_list = {"":0},
repair_list = {"":0},
science_list = {"":0},
strategy_list = {"":0},
suit_list = {"":0},
tactics_list = {"":0},
vehicle_list = {"":0}
)

Tokey = Char(
speed = 11,
analytical = 12,
creative = 16,
emotional = 14,
will = 11,
strength = 7,
dexterity = 11,
constitution = 12,
health = 12,
perception = 10,
height = 95,
width = 35,
length = 28,
weight = 16,
dr = 0,
acrobatics_skill = 0,
aerobatics_skill = 0,
aiding_skill = 1,
aquabatics_skill = 0,
arm_combat_skill = 2,
art_skill = 8,
attack_skill = 0,
chemistry_skill = 2,
climbing_skill = 3,
cooking_skill = 5,
cylaxian_skill = 10,
diplomacy_skill = 6,
disguise_skill = 0,
electrician_skill = 4,
electronic_operation_skill = 6,
engineering_skill = 0,
fast_draw_skill = 0,
games_skill = 3,
guns_skill = 0,
hobby_skill = 4,
math_skill = 5,
melee_weapon_skill = 0,
navigation_skill = 0,
naturalist_skill = 0,
physics_skill = 2,
repair_skill = 2,
science_skill = 5,
stealth_skill = 0,
strategy_skill = 0,
suit_skill = 0,
tactics_skill = 0,
vehicle_skill = 0,
writing_skill = 7,
gender = "Fale",
name = "Tokey",
race = race.Kan(),
languages = {"English":3},
damage = [0,0,0,0,0,0,0],
arms = True,
legs = True,
wings = False,
sight = True,
hearing = True,
feeling = True,
taste = True,
smell = True,
viberation = False,
poisoned = None,
pregnate = [False, 0, 0],
unconscious = False,
broken_arms = [False, 0],
broken_legs = [False, 0],
dazed = False,
short_curcuit = False,
broken_wings = [False, 0],
familiarities = {"":0},
traits = ["Claw"],
effects = [""],
cylax_tech = {"Carbon_Life":-1, "Electromotivate":3, "Kilo_Electromotivate":3, "Mega_Electromotivate":2, "Resilience":3},
cylax_value = bin(0),
items = [""],
arm_combat_list = {"":0},
art_list = {"Acting":-1, "Singing":1, "Piano Keyboard":0, "Movie Production":-2},
attack_list = {"":0},
cooking_list = {"Sea Sair Casual":0},
disguise_list = {"":0},
electronic_operation_list = {"Electricity Controllers":0, "General Computers":0},
engineering_list = {"":0},
fast_draw_list = {"":0},
games_list = {"KoKo Pops":0},
guns_list = {"":0},
hobby_list = {"Gaming":0},
math_list = {"Applied":0},
melee_weapon_list = {"":0},
navigation_list = {"":0},
naturalist_list = {"":0},
physics_list = {"":0},
repair_list = {"Power Lines":0},
science_list = {"Music Theory":0},
strategy_list = {"":0},
suit_list = {"":0},
tactics_list = {"":0},
vehicle_list = {"":0}
)

Lovlico = Char(
speed = 9,
analytical = 11,
creative = 9,
emotional = 11,
will = 12,
strength = 16,
dexterity = 11,
constitution = 12,
health = 11,
perception = 8,
height = 140,
width = 43,
length = 35,
weight = 24,
dr = 0,
acrobatics_skill = 6,
aerobatics_skill = 0,
aiding_skill = 0,
aquabatics_skill = 0,
arm_combat_skill = 7,
art_skill = 4,
attack_skill = 0,
chemistry_skill = 0,
climbing_skill = 1,
cooking_skill = 4,
cylaxian_skill = 0,
diplomacy_skill = 0,
disguise_skill = 0,
electrician_skill = 0,
electronic_operation_skill = 0,
engineering_skill = 0,
fast_draw_skill = 0,
games_skill = 1,
guns_skill = 0,
hobby_skill = 1,
math_skill = 2,
melee_weapon_skill = 0,
navigation_skill = 0,
naturalist_skill = 4,
physics_skill = 1,
repair_skill = 0,
science_skill = 0,
stealth_skill = 0,
strategy_skill = 0,
suit_skill = 0,
tactics_skill = 0,
vehicle_skill = 0,
writing_skill = 3,
gender = "Fale",
name = "Lovlico",
race = race.Kan(),
languages = {"English":3},
damage = [0,0,0,0,0,0,0],
arms = True,
legs = True,
wings = False,
sight = True,
hearing = True,
feeling = True,
taste = True,
smell = True,
viberation = False,
poisoned = None,
pregnate = [False, 0, 0],
unconscious = False,
broken_arms = [False, 0],
broken_legs = [False, 0],
dazed = False,
short_curcuit = False,
broken_wings = [False, 0],
familiarities = {"":0},
traits = ["Claw"],
effects = [""],
cylax_tech = {"Carbon_Life":-1},
cylax_value = bin(0),
items = [""],
arm_combat_list = {"Wrestling":0},
art_list = {"Wrestling Conplay":0},
attack_list = {"":0},
cooking_list = {"Cocha":0},
disguise_list = {"":0},
electronic_operation_list = {"General Computers":1, "Studio Workshop":0},
engineering_list = {"":0},
fast_draw_list = {"":0},
games_list = {"Combatslug":0},
guns_list = {"":0},
hobby_list = {"Combatslug":0},
math_list = {"Applied":0},
melee_weapon_list = {"":0},
navigation_list = {"":0},
naturalist_list = {"Realm":0},
physics_list = {"":0},
repair_list = {"":0},
science_list = {"":0},
strategy_list = {"":0},
suit_list = {"":0},
tactics_list = {"":0},
vehicle_list = {"":0}
)

Sevee = Char(
speed = 12,
analytical = 13,
creative = 13,
emotional = 10,
will = 13,
strength = 13,
dexterity = 15,
constitution = 12,
health = 12,
perception = 11,
height = 118,
width = 38,
length = 32,
weight = 21,
dr = 0,
acrobatics_skill = 6,
aerobatics_skill = 0,
aiding_skill = 0,
aquabatics_skill = 0,
arm_combat_skill = 3,
art_skill = 0,
attack_skill = 0,
chemistry_skill = 0,
climbing_skill = 4,
cooking_skill = 0,
cylaxian_skill = 9,
diplomacy_skill = 2,
disguise_skill = 1,
electrician_skill = 0,
electronic_operation_skill = 0,
engineering_skill = 0,
fast_draw_skill = 4,
games_skill = 0,
guns_skill = 0,
hobby_skill = 3,
math_skill = 4,
melee_weapon_skill = 7,
navigation_skill = 5,
naturalist_skill = 5,
physics_skill = 0,
repair_skill = 0,
science_skill = 2,
stealth_skill = 5,
strategy_skill = 0,
suit_skill = 0,
tactics_skill = 3,
vehicle_skill = 0,
writing_skill = 0,
gender = "Fale",
name = "Sevee",
race = race.Kan(),
languages = {"English":3},
damage = [0,0,0,0,0,0,0],
arms = True,
legs = True,
wings = False,
sight = True,
hearing = True,
feeling = True,
taste = True,
smell = True,
viberation = False,
poisoned = None,
pregnate = [False, 0, 0],
unconscious = False,
broken_arms = [False, 0],
broken_legs = [False, 0],
dazed = False,
short_curcuit = False,
broken_wings = [False, 0],
familiarities = {"Slide Kick":3},
traits = ["Claw"],
effects = [""],
cylax_tech = {"Carbon_Life":-1, "Strength":3, "Velociate":3, "Resilience":3, "Super_Strength":1, "Super_Resilience":1, "Standate_Velociate":1},
cylax_value = bin(0),
items = ["Blue Cape", "Savior Sword"],
arm_combat_list = {"Swords":0},
art_list = {"":0},
attack_list = {"":0},
cooking_list = {"":0},
disguise_list = {"":0},
electronic_operation_list = {"General Computers":3},
engineering_list = {"":0},
fast_draw_list = {"":0},
games_list = {"Combatslug":0},
guns_list = {"":0},
hobby_list = {"Combatslug":0},
math_list = {"":0},
melee_weapon_list = {"":0},
navigation_list = {"Ground":0},
naturalist_list = {"Realm":0},
physics_list = {"":0},
repair_list = {"":0},
science_list = {"Biology":0},
strategy_list = {"":0},
suit_list = {"":0},
tactics_list = {"Infantry":0},
vehicle_list = {"":0}
)

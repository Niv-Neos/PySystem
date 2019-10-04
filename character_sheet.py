import math as mt
import numpy as np
import engine as eg
import species as sp

import common_species as race ### Insert Species at Race

class Char:

       def __init__(self):

              ### Base Functions

              Race = race.Race()

              ### Identity

              self.Name = "Char"

              ### Base Stats

              self.SPE = 10 + Race.SPEstat
              self.ANA = 10 + Race.ANAstat
              self.CRE = 10 + Race.CREstat
              self.EMO = 10 + Race.EMOstat
              self.WIL = 10 + Race.WILstat

              self.ST = 10 + Race.STstat
              self.DX = 10 + Race.DXstat
              self.CO = 10 + Race.COstat
              self.HT = 10 + Race.HTstat
              self.PE = 10 + Race.PEstat

              self.Species = Race.Name
              self.Type = Race.Type
              self.Gender = "Fale"
              self.Attraction = "Pansexual"

              self.Height = 100 ### in centimeters
              self.Width = 100
              self.Length = 100

              self.Weight = 100 ### in Kilograms

              ### Base Secondary

              self.HP = (self.CO*5) + (self.ST*2.5) + (self.HT*2.5) + Race.HPstat
              self.FP = self.HT * 10 + Race.FPstat
              self.MP = self.WIL * 10 + Race.MPstat

              self.Sanity = self.WIL * 10 + Race.Sanitystat
              self.Lust = self.WIL * 10 + Race.Luststat
              self.Fear = self.WIL * 10 + Race.Fearstat

              self.Damage = [0, 0, 0, 0, 0, 0] ### HP, FP, MP, Sanity, Lust, Fear

              self.Dodge = self.DX/2 + Race.Dodgestat
              self.Move = self.DX/2 + Race.Movestat

              self.Harm = (self.ST/2)*(mt.log(self.DX, 2)*mt.sqrt(mt.log(self.DX, 2)))
              self.HarmType = "Blunt"

              self.DR = 0 + Race.DRstat

              ### Base Third

              self.Tech_Level = 0
              self.Languages = {"Engrish":3} ### Rating, Language

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
              self.PREGNAUT = False
              self.UNCONSCIOUS = False
              self.BROKEN_ARMS = False
              self.BROKEN_LEGS = False
              self.BROKEN_WINGS = False

              ### Skills

              self.Acrobatics_Skill = 0
              self.Acrobatics = [(self.DX-5)+self.Acrobatics_Skill, [""]] ### [Rating,Species]

              self.Aerobatics_Skill = 0
              self.Aerobatics = [(self.DX-5)+self.Aerobatics_Skill, [""]] ### [Rating,Species]

              self.Aiding_Skill = 0
              self.Aiding = [(self.ANA-6)+self.Aiding_Skill, [""]] ### [Rating,Species]

              self.Aquabatics_Skill = 0
              self.Aquabatics = [(self.DX-5)+self.Aquabatics_Skill, [""]] ### [Rating,Species]

              self.Arm_Combat_Skill = 0
              self.Arm_Combat = [(self.DX-4)+self.Arm_Combat_Skill,[""]] ### [Rating,Speciality]

              self.Art_Skill = 0
              self.Art = [((self.CRE/2)-3)+((self.ANA/4)-2)+((self.EMO/4)-2)+self.Art_Skill,[""],self.Tech_Level] ### [Rating, Art, Tech Level]

              self.Attack_Skill = 0
              self.Attack = [(self.DX-3)+self.Attack_Skill] ### [Rating]

              self.Chemistry_Skill = 0
              self.Chemistry = [(self.ANA-6)+self.Chemistry_Skill,self.Tech_Level] ### [Rating,Tech Level]

              self.Climbing_Skill = 0
              self.Climbing = [((self.ST/4)-1)+((self.HT/4)-1)+((self.DX/2)-2)+self.Climbing_Skill,[""]] ### [Rating,Species]

              self.Cooking_Skill = 0
              self.Cooking = [((self.ANA/2)-2)+((self.CRE/2)-2)+self.Cooking_Skill,[""]] ### [Rating,Speciality]

              self.Diplomacy_Skill = 0
              self.Diplomacy = [((self.EMO-5)+self.Diplomacy_Skill)] ### [Rating]

              self.Disguise_Skill = 0
              self.Disguise = [(self.DX-2)+(self.ANA-2)+(self.EMO-2)+self.Disguise_Skill,[""],self.Tech_Level] ### [Rating,Species,Tech Level]

              self.Electrician_Skill = 0
              self.Electrician = [(self.ANA-5)+self.Electrician_Skill,self.Tech_Level] ### [Rating,Tech Level]

              self.Electronic_Operation_Skill = 0
              self.Electronic_Operation = [(self.ANA-4)+self.Electronic_Operation_Skill,[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Engineering_Skill = 0
              self.Engineering = [(((self.ANA/2)-3)+((self.CRE/2))-3)+self.Engineering_Skill,[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Fast_Draw_Skill = 0
              self.Fast_Draw = [(self.DX-4)+self.Fast_Draw_Skill,[""]] ### [Rating,Speciality]

              self.Games_Skill = 0
              self.Games = [(((self.ANA/2)-2)+((self.CRE/2)-2))+self.Games_Skill,[""],self.Tech_Level] ### [Rating,Game,Tech Level]

              self.Guns_Skill = 0
              self.Guns = [(self.DX-4)+self.Guns_Skill,[""],[""],self.Tech_Level] ### [Rating,Weapon,Gun Type,Tech Level]

              self.Hobby_Skill = 0
              self.Hobby = [(((self.ANA/2)-2)+((self.CRE/2)-2))+self.Hobby_Skill,[""],self.Tech_Level] ### [Rating,Game,Tech Level]

              self.Math_Skill = 0
              self.Math = [(self.ANA-5)+self.Math_Skill,[""]] ### [Rating,Speciality]

              self.Melee_Weapon_Skill = 0
              self.Melee_Weapon = [(self.DX-4)+self.Melee_Weapon_Skill,[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Navigation_Skill = 0
              self.Navigation = [((self.ANA/3)-2)+((self.SPE/3)-2)+((self.PE/3)-2),[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Naturalist_Skill = 0
              self.Naturalist = [(((self.ANA/2)-3)+((self.CRE/2)-3))+self.Naturalist_Skill,[""]] ### [Rating,Bio Type]

              self.Physics_Skill = 0
              self.Physics = [(self.ANA-6)+self.Physics_Skill,[""],self.Tech_Level] ### [Rating,Field,Tech Level]

              self.Repair_Skill = 0
              self.Repair = [(self.ANA-6)+self.Repair_Skill,[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Science_Skill = 0
              self.Science = [(self.ANA-5)+self.Science_Skill,[""],self.Tech_Level] ### [Rating,Field,Tech Level]

              self.Stealth_Skill = 0
              self.Stealth = [self.Stealth_Skill] ### [Rating,Speciality,Tech Level]

              self.Strategy_Skill = 0
              self.Strategy = [((self.ANA/2)-3)+((self.CRE/2)-3)+self.Strategy_Skill,[""]] ### [Rating,Combat Situation]

              self.Suit_Skill = 0
              self.Suit = [(self.DX-4)+self.Suit_Skill,[""],self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Tactics_Skill = 0
              self.Tactics = [((self.ANA/2)-3)+((self.CRE/2)-3)+self.Strategy_Skill,[""]] ### [Rating,Combat Situation]

              self.Vehicle_Skill = 0
              self.Vehicle = [(self.DX-5)+self.Vehicle_Skill,[""],self.Tech_Level] ### [Rating,Type,Tech Level]

              self.Writing_Skill = 0
              self.Writing = [((self.ANA-4)+self.Writing_Skill)*(self.Languages[""]/3),self.Tech_Level] ### [Rating,Tech Level] Insert Language in the brackets of self.Languages


              '''
              Insert all familiarities they know and what level.
              1 - Beginner
              2 - Interminate
              3 - Expert
              '''

              self.familiaritie = {"I Know Something":3}

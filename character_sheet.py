import math as mt
import numpy as np

class Char:

       def __init__(self):

              ### Identity

              self.Name = Name

              ### Base Stats

              self.SPE = 10
              self.ANA = 10
              self.CRE = 10
              self.EMO = 10
              self.WIL = 10

              self.ST = 10
              self.DX = 10
              self.CO = 10
              self.HT = 10
              self.PE = 10

              self.Species = Species
              self.Gender = Gender
              self.Type = Type

              ### Base Secondary

              self.HP = (self.CO*5) + (self.ST*2.5) + (self.HT*2.5)
              self.FP = self.HT * 10
              self.MP = self.WIL * 10

              self.Sanity = self.WIL * 10
              self.Lust = self.WIL * 10

              self.dodge = self.DX
              self.move = DX/2

              self.size = 100 ### in centimeters

              ### Base Third

              self.Tech_Level = 0
              self.languages = [3,"Engrish"] ### Rating, Language

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

              self.POISON = None
              self.PREGNAUT = False
              self.UNCONSCIOUS = False
              self.BROKEN_ARMS = False
              self.BROKEN_LEGS = False
              self.BROKEN_WINGS = False

              ### Skills

              self.Acrobatics_Skill = 0
              self.Acrobatics = [(DX-5)+self.Acrobatics_Skill, ""] ### [Rating,Species]

              self.Aerobatics_Skill = 0
              self.Aerobatics = [(DX-5)+self.Aerobatics_Skill, ""] ### [Rating,Species]

              self.Aquabatics_Skill = 0
              self.Aquabatics = [(DX-5)+self.Aquabatics_Skill, ""] ### [Rating,Species]

              self.Arm_Combat_Skill = 0
              self.Arm_Combat = [(DX-4)+self.Arm_Combat_Skill,""] ### [Rating,Speciality]

              self.Art_Skill = 0
              self.Art = [((CRE/2)-3)+((ANA/4)-2)+((EMO/4)-2)+self.Art_Skill,"",self.Tech_Level] ### [Rating, Art, Tech Level]

              self.Attack_Skill = 0
              self.Attack = [(DX-3)+self.Attack_Skill] ### [Rating]

              self.Chemistry_Skill = 0
              self.Chemistry = [(ANA-6)+self.Chemistry_Skill,self.Tech_Level] ### [Rating,Tech Level]

              self.Climbing_Skill = 0
              self.Climbing = [((ST/4)-1)+((HT/4)-1)+((DX/2)-2)+self.Climbing_Skill,""] ### [Rating,Species]

              self.Cooking_Skill = 0
              self.Cooking = [((ANA/2)-2)+((CRE/2)-2)+self.Cooking_Skill,""] ### [Rating,Speciality]

              self.Diplomacy_Skill = 0
              self.Diplomacy = [((EMO-5)+self.Diplomacy_Skill)] ### [Rating]

              self.Disguise_Skill = 0
              self.Disguise = [(DX-2)+(ANA-2)+(EMO-2)+self.Disguise_Skill,"",self.Tech_Level] ### [Rating,Species,Tech Level]

              self.Electrician_Skill = 0
              self.Electrician = [(ANA-5)+self.Electrician_Skill,self.Tech_Level] ### [Rating,Tech Level]

              self.Electronic_Operation_Skill = 0
              self.Electronic_Operation = [(ANA-4)+self.Electronic_Operation_Skill,"",self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Engineering_Skill = 0
              self.Engineering = [(((ANA/2)-3)+((CRE/2))-3)+self.Engineering_Skill,"",self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Fast_Draw_Skill = 0
              self.Fast_Draw = [(DX-4)+self.Fast_Draw_Skill,""] ### [Rating,Speciality]

              self.Games_Skill = 0
              self.Games = [(((ANA/2)-2)+((CRE/2)-2))+self.Games_Skill,"",self.Tech_Level] ### [Rating,Game,Tech Level]

              self.Guns_Skill = 0
              self.Guns = [(DX-4)+self.Guns_Skill,"","",self.Tech_Level] ### [Rating,Weapon,Gun Type,Tech Level]

              self.Hobby_Skill = 0
              self.Hobby = [(((ANA/2)-2)+((CRE/2)-2))+self.Hobby_Skill,"",self.Tech_Level] ### [Rating,Game,Tech Level]

              self.Math_Skill = 0
              self.Math = [(ANA-5)+self.Math_Skill,""] ### [Rating,Speciality]

              self.Melee_Weapon_Skill = 0
              self.Melee_Weapon = [(DX-4)+self.Melee_Weapon_Skill,"",self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Naturalist_Skill = 0
              self.Naturalist = [(((ANA/2)-3)+((CRE/2)-3))+self.Naturalist_Skill,""] ### [Rating,Bio Type]

              self.Physics_Skill = 0
              self.Physics = [(ANA-6)+self.Physics_Skill,"",self.Tech_Level] ### [Rating,Field,Tech Level]

              self.Repair_Skill = 0
              self.Repair = [(ANA-6)+self.Repair_Skill,"",self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Science_Skill = 0
              self.Science = [(ANA-5)+self.Science_Skill,"",self.Tech_Level] ### [Rating,Field,Tech Level]

              self.Stealth_Skill = 0
              self.Stealth = [self.Stealth_Skill] ### [Rating,Speciality,Tech Level]

              self.Strategy_Skill = 0
              self.Strategy = [((ANA/2)-3)+((CRE/2)-3)+self.Strategy_Skill,""] ### [Rating,Combat Situation]

              self.Suit_Skill = 0
              self.Suit = [(DX-4)+self.Suit_Skill,"",self.Tech_Level] ### [Rating,Speciality,Tech Level]

              self.Tactics_Skill = 0
              self.Tactics = [((ANA/2)-3)+((CRE/2)-3)+self.Strategy_Skill,""] ### [Rating,Combat Situation]

              self.Vehicle_Skill = 0
              self.Vehicle = [(DX-5)+self.Vehicle_Skill,"",self.Tech_Level] ### [Rating,Type,Tech Level]

              self.Writing_Skill = 0
              self.Writing = [((ANA-4)+self.Writing_Skill)*(self.languages[0]/3),"",self.Tech_Level] ### [Rating,Language,Tech Level]

              ### Items

              self.Carrying_Items = ["Dust"]

              '''
              Insert all familiarities they know and what level.
              1 - Beginner
              2 - Interminate
              3 - Expert
              '''

              self.familiaritie = np.dtype([("I Know Something":3)])

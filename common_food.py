import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

class Food:

    def __init__(self, hp = 0, height = 1, width = 1, length = 1, weight = 1, calories = 0, fat = 0, sodium = 0, sugar = 0,
                    protein = 0, name = "", discription = "", vegetable = False, fruit = False, meat = False, grain = False,
                    damage = [0], flammable = False, poisonous = [False, []], raw_eatable = True, cook_eatable = True, moist = False):

        self.Name = name
        self.Discription = discription

        self.Vegetable = vegetable
        self.Fruit = fruit
        self.Meat = meat
        self.Grain = grain

        ### Stats

        self.HP = hp

        self.Damage = damage ### 0 = HP

        self.Calories = calories
        self.Fat = fat
        self.Sodium = sodium
        self.Sugar = sugar
        self.Protein = protein

        self.Height = height ### in centimeters
        self.Width = width
        self.Length = length
        self.Volume = self.Height * self.Width * self.Length

        self.Weight = weight

        ### Traits

        self.FLAMMABLE = flammable
        self.POISONOUS = poisonous ### Apply to what
        self.RAW_EATABLE = raw_eatable
        self.COOK_EATABLE = cook_eatable
        self.MOIST = moist

Korn_Meat = Food(
hp = 10,
height = 2,
width = 10,
length = 12,
weight = 1,
calories = 750,
fat = 45,
sodium = 2,
sugar = 0,
protein = 34,
name = "Korn Meat",
discription = "A steak of the fat Korn species. High in protein and fat.",
vegetable = False,
fruit = False,
meat = True,
grain = False,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False
)

Plub = Food(
hp = 8,
height = 9.25,
width = 10.15,
length = 9.25,
weight = 0.2,
calories = 100,
fat = 1.4,
sodium = 0,
sugar = 27,
protein = 0.2,
name = "Plub",
discription = "A round, sweet, red fruit.",
vegetable = False,
fruit = True,
meat = False,
grain = False,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = True,
moist = False
)

Kelp = Food(
hp = 8,
height = 0.55,
width = 2,
length = 18,
weight = 0.15,
calories = 90,
fat = 1.2,
sodium = 1,
sugar = 0.4,
protein = 1.0,
name = "Kelp",
discription = "A long, green vegetable.",
vegetable = True,
fruit = False,
meat = False,
grain = False,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = False,
moist = False
)

Nuc_and_Powder = Food(
hp = 30,
height = 6,
width = 10,
length = 10,
weight = 0.21,
calories = 450,
fat = 10.1,
sodium = 12,
sugar = 2,
protein = 4,
name = "Nuc and Powder",
discription = "Hot tunnel noodle with mussal powder liquidized in a hot bowl",
vegetable = False,
fruit = False,
meat = False,
grain = True,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = False,
cook_eatable = True,
moist = True
)

Bunny = Food(
hp = 20,
height = 6,
width = 9,
length = 9,
weight = 0.16,
calories = 1150,
fat = 27.5,
sodium = 9,
sugar = 13,
protein = 18,
name = "Bunny",
discription = "Processed meat in a sweet bun, with vegetables.",
vegetable = True,
fruit = False,
meat = True,
grain = True,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = False,
cook_eatable = True,
moist = False
)

Cereal = Food(
hp = 30,
height = 6,
width = 10,
length = 10,
weight = 0.11,
calories = 340,
fat = 5.25,
sodium = 3.5,
sugar = 9,
protein = 4,
name = "Cereal",
discription = "Grains within a bowl.",
vegetable = False,
fruit = False,
meat = False,
grain = True,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = False,
moist = False
)

Vegetable_Salad = Food(
hp = 25,
height = 8,
width = 14,
length = 14,
weight = 0.15,
calories = 280,
fat = 1,
sodium = 0.7,
sugar = 0.16,
protein = 0.8,
name = "Vegetable Salad",
discription = "A bowl of various vegetables.",
vegetable = True,
fruit = False,
meat = False,
grain = False,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = False,
moist = False
)

Fruit_Salad = Food(
hp = 25,
height = 7,
width = 12,
length = 12,
weight = 0.3,
calories = 330,
fat = 1.4,
sodium = 0.4,
sugar = 17,
protein = 2,
name = "Fruit Salad",
discription = "A bowl of various fruits.",
vegetable = False,
fruit = True,
meat = False,
grain = False,
damage = [0],
flammable = True,
poisonous = [False, []],
raw_eatable = True,
cook_eatable = False,
moist = False
)

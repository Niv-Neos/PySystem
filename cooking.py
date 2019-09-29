import math as mt
import numpy as np
import random as rd

### Import the Character here
import character_sheet as char
import common_food as food

Success = S
Cooker = char.Char()
Food_Item = food.Food()

Rating = Cooker.Cooking[0] ### (r)
Personal = ### Enter Personality and Emotional Factors (p)
Extra_Against = ### Any Additional Factors (e_n)
Extra_For = ### Any Additional Factors (e_d)

Difficulty = 0 ### (d)

Familiarity = ### How well they know the recipe (f)
Technology = ### Quality of the Technology (t)

S = ((Rating + Personal) * rd.randint(0.8,1.2)) - (Difficulty * (1 + Extra_Against / (Familiarity * Technology * Extra_For)))

if S > 0 and <= 5:
    print(Cooker.Name, "successifully cooked the", Food_Item.Name, ". It's decent quality.")

if S > 5 and <= 12:
    print(Cooker.Name, "successifully cooked a delicious meal of", Food_Item.Name, ". It's good quality.")

if S > 12 and <= 18:
    print(Cooker.Name, "successifully cooked an amazing meal of", Food_Item.Name, ". It's great quality")

if > 18:
    print(Cooker.Name, "made and outstanding meal of", Food_Item.Name, ". It's excellent quality.")

if S < 0:
    rd.randint(1,100)
    if Food_Item.FLAMMABLE is True and roll >= 1 and < 6:
        if S >= -4 and < 0:
            print(Cooker.Name,"burnt the", Food_Item.Name, "but it still eatable. Its poor quality.")
        elif S >= -9 and < -4:
            print(Cooker.Name, "burn the", Food_Item.Name, "to a crisp. It's uneatable.")
        elif S < -9:
            print(Cooker.Name, "set the food on fire!", Food_Item.Name, "is uneatable and in flames.")

    else:
        print(Cooker.Name, "made a bad meal.", Food_Item.Name, "is uneatable.")

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

S = ((Rating + Personal) * round(rd.uniform(0.80,1.20), 2)) - (Difficulty * (1 + Extra_Against / (Familiarity * Technology * Extra_For)))

print(S)

if S > 0 and <= 5:
    print(Cooker.Name, "successifully cooked the", Food_Item.Name, ". It's decent quality.")

if S > 5 and <= 12:
    print(Cooker.Name, "successifully cooked a delicious meal of", Food_Item.Name, ". It's good quality.")

if S > 12 and <= 18:
    print(Cooker.Name, "successifully cooked an amazing meal of", Food_Item.Name, ". It's great quality")

if > 18:
    print(Cooker.Name, "made and outstanding meal of", Food_Item.Name, ". It's excellent quality.")

if Food_Item.COOK_EATABLE is False and (Cooker.Naturalist[0] > 9 or (Cooker.Science[0] > (11 - (Cooker.ANA/3 - Cooker.PE/3)) and "Biology" in Cooker.Science[1] is True)):
    if Food_Item.RAW_EATABLE is True:
        print("But you notice that this is uneatable now and can only be eaten raw.")
    else:
        print("But you notice that this is still uneatable.")

if Food_Item.POISONOUS[0] is True and S > (10 - Cooker.ANA/2 - Cooker.PE/2):
    print("You also find out that", Food_Item.Name, "is poisonous to", Food_Item.POISONOUS[1])

if S < 0:
    rd.randint(1,100)
    if Food_Item.FLAMMABLE is True and roll >= 1 and < 20:
        if S >= -4 and < 0:
            print(Cooker.Name,"burnt the", Food_Item.Name, "but it still eatable. It's poor quality.")
        elif S >= -9 and < -4:
            print(Cooker.Name, "burn the", Food_Item.Name, "to a crisp. It's uneatable.")
        elif S < -9:
            print(Cooker.Name, "set the food on fire!", Food_Item.Name, "is uneatable and in flames.")

    if Food_Item.MOIST is True and roll >= 20 and < 51:
        if S >= -4 and < 0:
            print(Food_Item.Name, "have dried out. Now it's poor quality.")
        elif S < -4:
            print(Food_Item.Name, "have dried out and is completely spoiled. Now it's uneatable.")

    else:
        if S >= -5 and < 0:
            print(Cooker.Name, "made a bad meal.", Food_Item.Name, "is poor quality.")
        elif S < -5:
            print(Cooker.Name, "made a horrible meal.", Food_Item.Name, "is uneatable.")

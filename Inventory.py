import math as mt
import numpy as np
import random as rd
import engine as eg

'''
This is an inventory system for characters. Copy this file for each characters that will be
carrying inventory space.
Make sure to import each item module into the inventory to upload those items.

If your carrier have multiple pockets, make an additional self.Items and for self.Weight, add all the
dictionaries combined.
'''

import character_sheet as char
import common_items as items
import common_food as food

Carrier = char.Char()

### List items

Item_1 = items.Items()
Item_2 = food.Poison_Fruit()

class Backpack:

    def __init__(self):

        self.Name = "Backpack"

        self.SpaceHeight = 100 ### in centimeters
        self.SpaceWidth = 100
        self.SpaceLength = 100

        self.Volume = self.SpaceHeight * self.SpaceWidth * self.SpaceLength

        self.Items = {Item_1.Name : Item_1.Weight,
                        Item_2.Name : Item_2.Weight}

        self.Weight = 1 + sum(self.Items.values()))

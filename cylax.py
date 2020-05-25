import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')
'''
This is a calling code for using cylax
'''

'''
Placeholder
[“halogens”, “noble gases”, “nonmetals”, “transition metals”, “alkali metals”, “alkaline earth metals”, “post transition metals”, “metalloid”]
'''

### Objects

class Sector:

    def __init__(self):

        self.Name = ""
        self.Atoms = []
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Water:

    def __init__(self):

        self.Name = "Water"
        self.Atoms = ["reactive nonmetal"]
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Metal:

    def __init__(self):

        self.Name = "Metal"
        self.Atoms = ["transition metals"]
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Plastic:

    def __init__(self):

        self.Name = "Plastic"
        self.Atoms = ["reactive nonmetal"]
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Electronics:

    def __init__(self):

        self.Name = "Plastic"
        self.Atoms = ["reactive nonmetal", "transition metals"]
        self.Intelligence = 1 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Post_Metal:

    def __init__(self):

        self.Name = "Post Metal"
        self.Atoms = ["post transition metals"]
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Rock:

    def __init__(self):

        self.Name = "Rock"
        self.Atoms = ["halogens", "noble gases", "nonmetals", "transition metals", "alkali metals", "alkaline earth metals",
                      "post transition metals", "metalloid"]
        self.Intelligence = 0 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

class Carbon_Life:

    def __init__(self):

        self.Name = "Carbon Life"
        self.Atoms = ["halogens", "noble gases", "nonmetals", "transition metals", "alkali metals", "alkaline earth metals",
                      "post transition metals", "metalloid"]
        self.Intelligence = 2 ### 0 = No Intelligence, 1 = Electronic, 2 = Neuron

        self.Value = bin(0) ### 0 to 15 as it's 4 bit

### Techniques

class Tech:

    def __init__(self):

        self.Name = ""
        self.Value = bin(0) ### 0000
        self.Description = ""
        self.Ruling = ""
        self.Keywords = [""]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "DR for 1 second")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "DR for 1 second")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii/2, "DR for 1 second")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Reback:

    def __init__(self):

        self.Name = "Reback"
        self.Value = bin(0) ### 0000
        self.Description = "Return to the 0000 state."
        self.Ruling = "Power Action."
        self.Keywords = [""]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You reset your Cylax value to 0000 and you can't make an action until the end of the turn after your next.")
            if skill == 2:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You reset your Cylax value to 0000 and you can't make an action until the end of your next turn.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You reset your Cylax value to 0000.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")


class Strength:

    def __init__(self):

        self.Name = "Strength"
        self.Value = bin(2) ### 0010
        self.Description = "Enhance the strength of the inaugurator."
        self.Ruling = "Free action."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "ST for 1 second.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "ST for 1 second.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii/2, "ST for 1 second.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Super_Strength:

    def __init__(self):

        self.Name = "Super Strength"
        self.Value = bin(3) ### 0011
        self.Description = "Greatly enhance the strength of the inaugurator."
        self.Ruling = "Free action."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii, "ST for 1 second and you can only make one action before the beginning of your next turn.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii, "ST for 1 second and you can only make one action before the beginning of your next turn.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] + character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii, "ST for 1 second and you can only make one action before the beginning of your next turn.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Resilience:

    def __init__(self):

        self.Name = "Resilience"
        self.Value = bin(12) ### 1100
        self.Description = "Create a defensive force around inaugurator."
        self.Ruling = "Require a reaction action."
        self.Keywords = ["Atomics"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "additional DR for 1 second.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "additional DR for 1 second.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii/2, "additional DR for 1 second.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Super_Resilience:

    def __init__(self):

        self.Name = "Super Resilience"
        self.Value = bin(13) ### 1101
        self.Description = "Create a great defensive force around inaugurator."
        self.Ruling = "Require a reaction action."
        self.Keywords = ["Atomics"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii, "additional DR for 1 second. You can't make an action until the end of your next turn.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii, "additional DR for 1 second. You can't make an action until the end of your next turn.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii, "additional DR for 1 second. You can't make an action until the end of your next turn.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Presistent_Resilience:

    def __init__(self):

        self.Name = "Presistent Resilience"
        self.Value = bin(13) ### 1101
        self.Description = "Create a defensive force around inaugurator for an extended amount of time."
        self.Ruling = "Require a power action."
        self.Keywords = ["Atomics"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "additional DR for", 1 + character.Cylax_Tech[self.Name],"seconds. You can't make an action until the beginning of your next turn.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You get", skill_ii/2, "additional DR for", 1 + character.Cylax_Tech[self.Name], "seconds. You can't make an action until the beginning of your next turn.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You get", skill_ii/2, "additional DR for", 1 + character.Cylax_Tech[self.Name], "seconds. You can't make an action until the beginning of your next turn.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Combustion:

    def __init__(self):

        self.Name = "Combustion"
        self.Value = bin(2) ### 0010
        self.Description = "Inflicting a heated fueling agent across a substence to cause fire."
        self.Ruling = "Power Action."
        self.Keywords = ["Thermodynamics"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Create a stream of fire at an area of up to", skill_ii/45, "meters^2, at up to", (skill_ii/2)+590, "temperture.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Create a stream of fire at an area of up to", skill_ii/30, "meters^2, at up to", (skill_ii/2)+590, "temperture.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("Create a stream of fire at an area of up to", skill_ii/15, "meters^2, at up to", (skill_ii/2)+590, "temperture.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Electromotivate:

    def __init__(self):

        self.Name = "Electromotivate"
        self.Value = bin(2) ### 0010
        self.Description = "Cause pressure on atom to cause an electrical charge."
        self.Ruling = "Power Action."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/3, "meters^2, at up to,", skill_ii, "pressure.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/2, "meters^2, at up to,", skill_ii*2, "pressure.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("Electrify an area of", skill_ii, "meters^2, at up to,", skill_ii*3, "pressure.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Greater_Electromotivate:

    def __init__(self):

        self.Name = "Greater Electromotivate"
        self.Value = bin(3) ### 0011
        self.Description = "Cause pressure on atom to cause a greater electrical charge."
        self.Ruling = "Power Action, Restand."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 40)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/3, "meters^2, at up to,", skill_ii*2, "pressure.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 25)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/2, "meters^2, at up to,", skill_ii*4, "pressure.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("Electrify an area of", skill_ii, "meters^2, at up to,", skill_ii*6, "pressure.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Kilo_Electromotivate:

    def __init__(self):

        self.Name = "Kilo Electromotivate"
        self.Value = bin(7) ### 0101
        self.Description = "Cause pressure on atom to cause a kilo level electrical charge."
        self.Ruling = "Power Action, Restand."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 50)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/3, "meters^2, at up to,", skill_ii*20, "pressure.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/2, "meters^2, at up to,", skill_ii*50, "pressure.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("Electrify an area of", skill_ii, "meters^2, at up to,", skill_ii*100, "pressure.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Mega_Electromotivate:

    def __init__(self):

        self.Name = "Mega Electromotivate"
        self.Value = bin(8) ### 0111
        self.Description = "Cause pressure on atom to cause a mega level electrical charge."
        self.Ruling = "Power Action, Restand."
        self.Keywords = ["Electricity"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 60)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/3, "meters^2, at up to,", skill_ii*20000, "pressure.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 45)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("Electrify an area of", skill_ii/2, "meters^2, at up to,", skill_ii*50000, "pressure.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("Electrify an area of", skill_ii, "meters^2, at up to,", skill_ii*100000, "pressure.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Rerend:

    def __init__(self):

        self.Name = "Rerend"
        self.Value = bin(2) ### 0010
        self.Description = "Heal the cells of a biological organism."
        self.Ruling = "Power Action. Range 5 meters."
        self.Keywords = ["Bio"]

    def Inaugurate(self, character, target):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You heal the target for", skill_ii/3, "HP.")
                    target.Damage[0] = target.Damage[0] - skill_ii/3
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You heal the target for", skill_ii/2, "HP.")
                    target.Damage[0] = target.Damage[0] - skill_ii/2
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You heal the target for", skill_ii, "HP.")
                target.Damage[0] = target.Damage[0] - skill_ii
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Velociate:

    def __init__(self):

        self.Name = "Velociate"
        self.Value = bin(4) ### 0100
        self.Description = "Have yourself move."
        self.Ruling = "Power Action"
        self.Keywords = ["Pressure"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", skill_ii/3, "decimeters.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", skill_ii/2, "decimeters.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You move", skill_ii, "decimeters.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Standate_Velociate:

    def __init__(self):

        self.Name = "Standate Velociate"
        self.Value = bin(6) ### 0110
        self.Description = "Have yourself move greatly."
        self.Ruling = "Power Action, Restand."
        self.Keywords = ["Pressure"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", skill_ii/3, "meters.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", skill_ii/2, "meters.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You move", skill_ii, "meters.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

class Accelerate:

    def __init__(self):

        self.Name = "Accelerate"
        self.Value = bin(2) ### 0010
        self.Description = "Have yourself move while in motion."
        self.Ruling = "Free Action"
        self.Keywords = ["Pressure"]

    def Inaugurate(self, character):
        skill = character.Cylax_Tech[self.Name]
        Cost = eg.Cylax_Cost(self.Value)
        Checker = eg.Cylax_Able(character, self.Value)
        Checker.Check()
        if (Checker.Final is True):
            character.Damage[3] = character.Damage[3] + Cost.Result ### equal to the number of 1s in the binary.
            character.Cylax_Value = self.Value
            if skill == 1:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 30)
                Check = rd.randint(Cal_i,3)
                if Check < 2:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", (skill_ii/3)/2, "decimeters.")
            if skill == 2:
                Cal_i = eg.Minner(0, character.Cylaxian[0], 20)
                Check = rd.randint(Cal_i,2)
                if Check < 1:
                    print("You fail to inaugurate", self.Name)
                else:
                    skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                    print("You inaugurate", self.Name)
                    print("You move", (skill_ii/2)/2, "decimeters.")
            if skill == 3:
                skill_ii = character.Cylaxian[0] * character.Cylax_Tech[self.Name]
                print("You inaugurate", self.Name)
                print("You move", skill_ii/2, "decimeters.")
            else:
                print("Error: Not a valued skill level. Needs to match the character's skill on their character sheet at self.Cylax_Tech,")
                print("ranging from 1 to 3.")
        else:
            print("Unable to inaugurate as your bit state is", character.Cylax_Value, "and", self.Name , "is", self.Value, ".")

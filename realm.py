import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

sys.path.insert(1, 'C:/Users/Frank/Desktop/Cylax/PySystem')

'''
For more information about the inner contents of Realm, go to World/Realm
'''

class Realm:

    def __init__(self):

        self.Name = "Realm"       # For now :)

        # Orbital characteristics
        self.Aphelion = 152100000       # Furtherist from the sun
        self.Perihelion = 147095000      # Clostest from the sun
        self.Semi_major_axis = 149598023        # Middle dist

        self.Eccentricity = 0.0167086       # JUST LOOK IT UP >:(

        self.Average_orbital_speed = 29.78


        self.Inclination = 3.1452       #In degrees. Tilt from the sun

        self.Satellites = 1
        self.Quasi_satellites = 3
        self.Artifical_satellites = 1000
        self.Space_debris = 38524

        # Physical Characteristics
        self.Mean_radius = 6140.7
        self.Circumference = (mt.pi)/((self.Mean_radius)*2)
        self.Surface_area = 4*(mt.pi)*((self.Mean_radius)**2) # Square
        self.Volume = 4/(3*(mt.pi)*(self.Mean_radius**3)) # Cubic
        self.Mean_denisty = 5.514
        self.Mass = self.Volume/self.Mean_denisty

        self.Surface_gravity = ((6.674*(10**-11))*1*(self.Mass))/6140.7*2
        self.Mechanical_gravity = 1

Kan_names = [""]
Kan_gender = ["Fale", "Male", "Asexual", "Herm", "MtF", "FtM"]
realm = Realm()

'''
Physical = Realm()
print(Physical.Mean_radius)
print(Physical.Circumference)
print(Physical.Surface_area)
print(Physical.Volume)
print(Physical.Mean_denisty)
print(Physical.Mass)
print(Physical.Surface_gravity)
'''

import math as mt
import numpy as np
import random as rd
import engine as eg
import physics as ph
import cylax as cl
import sys
import config as cf

class Battery:
    def __init__(self, pressure, current, capacity, max_current, release, height = 1, width = 1, length = 1, name = "Battery"):
        self.Name = name
        self.Amount = pressure
        self.Current = current
        self.Storage = capacity
        self.Maximum_Current = max_current
        self.Charge = release
        self.Height = height ### in cm
        self.Length = length ### in cm
        self.Width = width ### in cm
        self.Volume = self.Height * self.Length * self.Width

    def Charging(self, current_ii = 0, resistance = 0, time = 0, overcharge_regulator = False):
        x = ph.Electrical_Charge(current_ii, resistance, time)
        Charging_Amount = x.energy ### pressure
        Required_for_Full = self.Storage - self.Amount
        self.Amount = self.Amount + (Charging_Amount * time)
        Result = Charging_Amount * time
        if current_ii > self.Maximum_Current:
            check_i = current_ii - self.Maximum_Current
            print(self.Name, "is being charged by something with greater current.")
            if check_i >= 1 and check_i < 11:
                print("The battery melts inside, it is now broken.")
            elif check_i >= 11 and check_i < 21:
                print("The battery gets set on fire and is broken.")
            elif check_i >= 21 and check_i < 31:
                print("Part of the battery explodes an emanation of", round(eg.Cuberoot(self.Volume)*2, 2))
            else:
                print("The entire battery explodes an emanation of", round(eg.Cuberoot(self.Volume)*3, 2))
        else:
            print(self.Name, "is charged for", time, "seconds, a total of,", Result, "pressure.")
            if self.Amount > self.Storage and overcharge_regulator is False:
                print(self.Name, "is overcharged by", self.Amount-self.Storage, "pressure.")
                check_i = self.Amount - self.Storage
                if check_i >= 1 and check_i < 11:
                    print("The battery melts inside, it is now broken.")
                elif check_i >= 11 and check_i < 21:
                    print("The battery gets set on fire and is broken.")
                elif check_i >= 21 and check_i < 31:
                    print("Part of the battery explodes an emanation of", round(eg.Cuberoot(self.Volume)*2, 2))
                else:
                    print("The entire battery explodes an emanation of", round(eg.Cuberoot(self.Volume)*3, 2))
            elif self.Amount > self.Storage and overcharge_regulator is True:
                self.Amount = self.Storage
                print(self.Name, "stop charging as it have reach full capacity.")
                print("It fully charged at", Required_for_Full/Charging_Amount, "seconds.")
                print(self.Name, "now have", self.Amount, "pressure.")
            else:
                print(self.Name, "now have", self.Amount, "pressure.")

    def Supply(self, time = 0):
        Requirement_for_Discharge = (self.Charge * time) - self.Amount
        RDO = self.Amount
        self.Amount = self.Amount - (self.Charge * time)
        if self.Amount < 0:
            self.Amount = 0
            print(self.Name, "decharged early at", time*(Requirement_for_Discharge/RDO), "seconds.")
        Result = self.Charge * time
        print(self.Name, "charges the object for", time, "seconds, a total of", Result, "pressure.")
        print(self.Name, "now has", self.Amount, "pressure.")


Nine_P_Battery = Battery(pressure = 28800, current = 0.550, capacity = 28800, max_current = 0.550,
                        release = 9, height = 4.85, width = 2.65, length = 1.75, name = "9P Battery")

Six_P_Battery = Battery(pressure = 14400, current = 0.550, capacity = 14400, max_current = 0.550,
                        release = 6, height = 3.15, width = 1.25, length = 0.95, name = "6P Battery")

Large_Twenty_P_Battery = Battery(pressure = 64000, current = 0.550, capacity = 64000, max_current = 0.550,
                        release = 20, height = 9.25, width = 5.00, length = 4.05, name = "20P Battery")

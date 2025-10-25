#!/usr/bin/env python3
#Carson Black
#033_C_4_3_8_lab_5_converting_fuel_consumption.py

import os
if os.name == "nt": os.system("cls")
else: os.system("clear")

MperMI = 1609.344 # meters per mile
MperKM = 1000 # meters per kilometer
KMper100KM = 100 # kilometers per 100 kilometers
LperGAL = 3.785411784 # Liters per gallon


def liters_100km_to_miles_gallon(liters):

    MIper100KM = (100 * MperKM) / MperMI
    GALper100KM = liters / LperGAL

    mpg = MIper100KM / GALper100KM
    #           ^-------------^
    # 100 km units cancel (one in numerator, one in denominator)

    return mpg

def miles_gallon_to_liters_100km(mpg):

    MIper100KM = (100 * MperKM) / MperMI
    GALper100KM = MIper100KM / mpg
    Lper100KM = GALper100KM * LperGAL

    return Lper100KM
# (L / gal) * (gal / mi) * (mi / 100km)
#       ^-------^     ^-----^
# Units cancel.  You are left with L / 100km.

testValues = [
    print(liters_100km_to_miles_gallon(3.9)),
    print(liters_100km_to_miles_gallon(7.5)),
    print(liters_100km_to_miles_gallon(10.)),
    print(miles_gallon_to_liters_100km(60.3)),
    print(miles_gallon_to_liters_100km(31.4)),
    print(miles_gallon_to_liters_100km(23.5))
]

#---Experiments below---

userConversion = input("Select conversion: L/100km--->mpg (L) or mpg--->L/100km (M)\n: ")
if userConversion in ("L", "M"):
    try:
        userValue = float(input("Enter value.\n: "))
        if userConversion == "L":
            print(f"{userValue} L/100km = {liters_100km_to_miles_gallon(userValue)} mpg.")
        elif userConversion == "M":
            print(f"{userValue} mpg = {miles_gallon_to_liters_100km(userValue)} L/100km.")
    except ValueError:
        print("Invalid input.")
else:
    print("Invalid input.")
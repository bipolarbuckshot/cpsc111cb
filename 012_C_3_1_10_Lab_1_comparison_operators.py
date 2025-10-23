#!usr/bin/env python3
#Carson Black
#012_C_3_1_10_Lab_1_comparison_operators.py

plant = input("Plant name\n: ")

if plant == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif plant == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathyphyllum! Not ", plant, "!", sep="")

#---Experiments below---

if plant == "Azalea":
    print("Actually, I might like Azaleas better anyway.")
else:
    pass # Demonstrating pass to skip else section
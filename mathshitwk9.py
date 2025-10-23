from fractions import Fraction
import os
os.system("clear")

# p is the constant (at the end)
p = [
    1,
    5
    ]
# q is the leading coefficient (the number attached to the highest degree variable)
q = [
    1,
    2,
    3,
    6
    ]

matrix = [[str(Fraction(i,j)) for i in p] for j in q]

width = max(len(str(frac)) for row in matrix for frac in row)


for row in matrix:
    print('  '.join(f"±{str(frac):>{width}}" for frac in row))

input("Press enter to clear...")
os.system("clear")
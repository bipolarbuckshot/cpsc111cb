#!usr/bin/env python3
#Carson Black
#022_C_3_3_1_tests_PART1.py

# I have no clue what exactly I'm supposed to do for this, but I'll just do some stuff anyway.

i = 15
j = 1
if i and j:
    print("1: True")
else:
    print("1: False")

if not(i) or not(j):
    print("Output 2")

bitneg = ~i # performs ~ on 15
print(bitneg)

i = 1
j = not not i # evaluates i as True (not 0), then inverts the value to False, then again to True
print(j)

m = 19
n = 4
p = 7

print(m&p) # Bitwise operators. This one is conjunction. (Both bits 1, output 1.)
print(m|p) # Disjuction. (If either bit is 1, output 1.)
print(m^p) # Exclusive or (XOR). (If exactly one of the bits is 1, output 1.)
#!usr/bin/env python3
#Carson Black
#003_C_2_3_3_operators.py

print(2**4) # This should raise 2 to the power of 4.
print(8 + 5) # 8 plus 5.
print(8 - 5) # 8 minus 5.
print(8 * 5) # 8 times 5.
print(8 / 5) # 8 divided by 5. Will result in a floating point number.
print(8 // 5) # 8 floor division into 5. Results in the rounded down integer from the float answer above.
print(8 % 5) # 8 modulo 5. Results in the remainder from above.
print(+5) # Unary operator.
print(-5) # Unary operator resulting in -5.

#---Experiments below---

print() # separator
print(-3 ** 2) # Outputs -9 when you might expect 9. It does the exponentiation before making the number negatibe (*-1).
print(16 % 6 % 3) # 16 modulo 3 is 4, then 4 modulo 3 is 1.
print(2 + 4 * 5) # Does the 4*5 first, then 2+ the result. 4*5=20, 20+2=22. If I wanted to add 2 to 4 then multiply, i would need parentheses.
print(( 2 + 4) * 5) # Like this. 2+4=6, 6*5=30.
print(2-3**2)
print(3**2-2)
print(3**(2-2)) # 3 to the zero power is 1, as with every other number.
print((3**2)-2) # 3 to the 2 power is 9, minus 2 is 7.
#!usr/bin/env python3
#Carson Black
#014_C_3_1_12_Lab_3_essentials_of_if_elif_else.py

year = int(input("Enter a year: "))

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
	if year % 4 != 0:
		print("Common year")
	elif year % 100 != 0:
		print("Leap year")
	elif year % 400 != 0:
		print("Common year")
	else:
		print("Leap year")

#---Experiments below---

# Using variables to accomplish the same job

print("Experiments below")

leap = False
greg = False

if year < 1582:
	print("Not within the Gregorian calendar period")
else:
    #  Write the if-elif-elif-else block here.
	greg = True # within the gregorian calendar
	if year % 4 != 0:
		leap = False
	elif year % 100 != 0:
		leap = True
	elif year % 400 != 0:
		leap = False
	else:
		leap = True
    
if leap and greg: # 'if leap' is equivalent to 'if leap = True'
    print("Leap year")
elif greg:
    print("Common year")
else:
	pass
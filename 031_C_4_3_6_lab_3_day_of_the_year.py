#!/usr/bin/env python3
#Carson Black
#031_C_4_3_6_lab_3_day_of_the_year.py


import os
def clearConsole():
    if os.name == "nt": os.system("cls")
    else: os.system("clear")
# Makes console much less cluttered and also makes me happy :)

clearConsole()

class tc: # My text color class from my midteerm
    R = '\033[91m' # Red
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    x = '\033[0m'  # reset code

# I made all of my varibles camelCase this time, I like it better.

def isYearLeap(year):
    return year % 400 == 0 or ( year % 100 != 0 and year % 4 == 0 )

def daysInMonth(year, month):

    days = [None,31,28,31,30,31,30,31,31,30,31,30,31] # List of month lengths, position 0 set to return None.

    if month not in range(1, 13):
        return None     # If month is any number that is not from 1 to 12, return None.
    if month == 2 and isYearLeap(year):
        return int(29)  # If month is 2 and year is leap, return 29 as an integer.
    
    return int(days[month]) # Otherwise, return the month length corresponding to the month's position in the list.

def dayOfYear(year, month, day):

    if year < 1: return None # Checking for invalid inputs

    monthLength = daysInMonth(year, month)
    if monthLength == None:
        return None
    if day < 1 or day > monthLength:
        return None

    totalDays = day

    for m in range(1, month):
        totalDays += daysInMonth(year, m)
    
    return totalDays # It took me 15 minutes to find out this line was missing .___.
    



loop = True
while loop: # haha it's funny because it says while loop
    try:
        # Error handling for dumb people that think "cheeseburger" is a year
        yr = int(input("Enter year: "))
        mo = int(input("Enter month: "))
        d = int(input("Enter day: "))

        loop = False
        break

    except ValueError:
        input(f"{tc.R}That won't work. After pressing enter, make sure to read the instructions...{tc.x}")
        clearConsole()

print()

print(f"Test data: {tc.Y}{yr}, {mo}, {d}{tc.x}")

print()

result = dayOfYear(yr, mo, d)
if result == None:
    print(f"{tc.R}Invalid date.{tc.x}")
else:
    print(f"{mo}/{d} is day {tc.Y}{result}{tc.x} in {yr}.")

print()

testValues = [
    (1900, 2, 29, None),  # 1900 not a leap year, no day 29 in February
    (2000, 2, 29, 60),    # 2000 is a leap year, no problem
    (2024, 12, 31, 366),  # 366 days in a leap year, testing to see if it counts that correctly
    (-1, 4, 20, None)     # There is a safeguard against negative numbers because history isn't real (hehe)
]

for i, (testYear, testMonth, testDay, testExpectation) in enumerate(testValues, start=1):
    # This took embarassingly long to figure out, I just wanted to be able to print i in my f-strings

    result = dayOfYear(testYear, testMonth, testDay)

    if result == testExpectation:
        print(f"Test value {i} {tc.G}passed{tc.x}.")
    else:
        print(f"Test value {i} {tc.R}failed{tc.x}.")

print()

# I recommend testing code with something like 2000 2 29 and 1999 2 29 to see everything at work.
# Experimentation throughout (formatting, features, etc.)
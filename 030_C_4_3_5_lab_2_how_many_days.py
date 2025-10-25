#!/usr/bin/env python3
#Carson Black
#030_C_4_3_5_lab_2_how_many_days.py


import os
if os.name == "nt": os.system("cls")
else: os.system("clear")
# Makes console much less cluttered and also makes me happy :)


class tc: # My text color class from my midteerm
    R = '\033[91m' # Red
    G = '\033[92m' # Green
    Y = '\033[93m' # Yellow
    x = '\033[0m'  # reset code


def is_year_leap(year):
    return \
        year % 400 == 0 \
        or \
        ( year % 100 != 0 and year % 4 == 0 )

def days_in_month(year, month):

    days = [None,31,28,31,30,31,30,31,31,30,31,30,31] # List of month lengths, position 0 set to return None.
    if month not in range(1, 13):         return None # If month is any number that is not from 1 to 12, return None.
    if month == 2 and is_year_leap(year): return int(29) # If month is 2 and year is leap, return 29 as an integer.
    return int(days[month]) # Otherwise, return the month length corresponding to the month's position in the list.

        # if month in (1,3,5,7,8,10,12): return int(31)
    # elif month in (4,6,9,11):      return int(30)
    # elif month == 2:
    #     if is_year_leap(year):     return int(29)
    #     else:                      return int(28)
    # else:                          return None

    # The above code is another way to accomplish the same thing.


print()

test_years = [1900, 2000, 2016, 1987, 4097]
test_years.append(int(input("Enter an additional year to test: ")))

test_months = [2, 2, 1, 11, 69]
test_months.append(int(input("Enter an additional month to test (int only): ")))

test_results = [28, 29, 31, 30, None]
user_val_is_leap = is_year_leap(test_years[-1])
test_results.append(days_in_month(test_years[-1], test_months[-1]))

print()

print("Test months: ", test_months)
print("Test years: ", test_years)
print("Test results: ", test_results)

print()

for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(f"{yr} - {mo}, -> ", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        if result == None:
            print(f"{tc.R}Invalid month{tc.x}")
            continue
        else:
            print(f"{tc.G}OK{tc.x}")
            print(f"  {tc.Y}{result} days in {mo}/{yr}.{tc.x}")
    else:
        print(f"{tc.R}Failed{tc.x}")

print()

# Experimentation can be found throughout.
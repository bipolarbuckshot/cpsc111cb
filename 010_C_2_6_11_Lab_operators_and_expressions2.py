#!/usr/bin/env python3
#Carson Black
#010_C_2_6_11_Lab_operators_and_expressions2.py


hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.

time_in_mins = (hour * 60) + mins

final_time = time_in_mins + dura # time in minutes

output_hour = final_time // 60 # divides and rounds down to get the hours back
output_mins = final_time % 60 # remainder of the line above

# if output_hour > 23: # Prevents hour readouts higher than 23, which don't exist in real life.
#    output_hour -= 24 # Only to a certain point.

output_hour = output_hour % 24 # This seems to work better.

print(str(output_hour) + ":" + str(output_mins)) # prints formatted time

#---Experiments below---

print("\nExperiments below:\n")

print(output_hour)
print(output_mins)

if output_mins < 10 and output_mins >= 0: # if the output_mins variable is between 0 and 9, it adds a zero before the minutes to make it display as time should normally.
    output_mins = "0" + str(output_mins)

print("The event starts at ", str(hour), ":", str(mins), " and ends at ", str(output_hour), ":", str(output_mins), ".", sep="")
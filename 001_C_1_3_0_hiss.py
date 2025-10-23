#!/usr/bin/env python3
#Carson Black
#001_C_1_3_0_hiss.py

#Prints message
print("Hisssssss...")
print("Oink...")
print("Mooooo...")

#------Experiments below this line------

print ()
print() #Looks like both work whether or not there is a space.
print(5+5) #You can add integers in a print function.
#print(5+"5") This doesn't work! Looks like you can't add strings and integers. Commented out with #.
print("5"+"5") #Adding numbers inside quotes just squishes them together.

#Requests user input with a prompt
hi = input("Hi! \nsay hello:  ") #'\n' brings the following text to a new line.

#If the response is 'hello', it will return 'yes', otherwise it will return 'no'
if hi == "hello": #You need two equal signs to make this work, one will not work.
    print("yes")
else:
    print("no")

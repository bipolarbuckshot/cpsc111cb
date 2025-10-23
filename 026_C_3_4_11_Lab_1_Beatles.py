#!usr/bin/env python3
#Carson Black
#026_C_3_4_11_Lab_1_Beatles.py

# step 1
beatles = []
print("Step 1:", beatles)

# step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# step 3
for i in range(2):
    member = input("Next band member:\n ")
    beatles.append(member)
print("Step 3:", beatles)

# step 4
del beatles[-1] # -1 removes the last element of the list
del beatles[-1]
print("Step 4:", beatles)

# step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))

#---Experiments below---

print(f"{beatles[(int(input("Enter an integer within the bounds of the band member list.\n: ")) - 1)]} is the best beatle.")
# subtracted 1 from the value to make it more accessible to humans.
# otherwise the values would start at zero.
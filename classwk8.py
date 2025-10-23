# row = ["WHITE_PAWN" for i in range(int(input("Number: ")))]
# print(row)


# row = []
# for i in range(8):
#     row.append("WHITE_PAWN")
# print(row)


# board = []
# for i in range(8):
#     row = ["EMPTY" for i in range(8)]
#     board.append(row)
# print(board)


# import numpy as np

# arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
# print(f"In the array, the value of row 1 column 2 is: {arr[1,2]}")
# arr[int(input("Enter integer for row: ")),int(input("Enter integer for column: "))] = int(input("Enter integer to replace value with: "))
# print(arr)


# howMany = [2 ** i for i in range(8)]
# print(howMany)

# print()

# whatsThis = [x for x in howMany if x%2!=0]
# print(whatsThis)


# howMany = [1,2,4,8,16,32,64,128]
# whatsThis = []
# for x in howMany:
#     if x%2!=0:
#         whatsThis.append(x)
#         print(whatsThis)


# for i in range(3):
#     print("#") # Prints 3 times
# else:
#     print("#") # Prints one more time


# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         try:
#             var/=0
#         except ZeroDivisionError:
#             print("You suck at coding!!. Dont /0.")
#     else:
#         print("#")


temps = [[(60+hours) for hours in range(24)] for day in range(31)]

total = 0.0

for day in temps:
    total += day[1]
    print(temps)

average = total / 31

print(f"Average noon temperature: {average}")
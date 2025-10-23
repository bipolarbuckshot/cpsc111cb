my_list = [1, 'a', ["list", 64, [0, 1], False]]
print(my_list)

my_list[1], my_list[2][3] = my_list[2][3], my_list[1]
print(my_list)